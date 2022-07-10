var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var indexRouter = require('./routes/index');
const dotenv = require('dotenv');
const celery = require('celery-node');
const mongoose = require('mongoose');
var amqp = require('amqplib/callback_api');
const Ping = require('./models/Ping');

const amqpUrl = process.env.AMQP_URL || 'amqp://localhost:5672';

const connectDB = async () => {
    try {
        const conn = await mongoose.connect(process.env.MONGO_URI,{
            useNewUrlParser: true,
            useUnifiedTopology: true
        });

        console.log(`MongoDb connected: ${conn.connection.host}`);
    } catch (error) {
        console.error(error);
        process.exit(1);
    }
};
dotenv.config({ path: './.env' });
connectDB();

const client = celery.createClient(amqpUrl, amqpUrl);
const celeryWorker = celery.createWorker(amqpUrl, amqpUrl);

amqp.connect(amqpUrl, function(error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function(error1, channel) {
    if (error1) {
      throw error1;
    }
    var queue = 'ping_indices';

    channel.assertQueue(queue, {
      durable: true
    });
    channel.prefetch(1);
    console.log(" [*] Waiting for messages in %s...", queue);
    channel.consume(queue, function(msg) {
      console.log(" [x] Received %s", msg.content);
      const data = JSON.parse(msg.content.toString());
      const pingId = data.pingId;

      let sidi = 0.0;
      let siin = 0.0;

      const notEmpty = (obj) => Object.keys(obj).length > 0;
      if (notEmpty(data.fromLocations) && notEmpty(data.toLocations)) {
        sidi = calcSidiIndex(
          Object.values(data.fromLocations),
          Object.values(data.toLocations)
        ); 
      }
      if (notEmpty(data.fromTags) && notEmpty(data.toTags)) {
        siin = calcSiinIndex(
          data.fromTags,
          data.toTags
        );
      }
      console.log(' [x] sidi:', sidi);
      console.log(' [x] siin:', siin);
      client.createTask("tasks.calcDindinIndex")
            .applyAsync([pingId, sidi, siin])
            .get().then(data => {
              console.log(data);
            });
      channel.ack(msg);
    }, {
      noAck: false
    });
  });
});

function calcSidiIndex(p1, p2) {
  const cx1 = p1.map((p) => p[0]).reduce(
    (prev, current) => prev + current
  );
  const cy1 = p1.map((p) => p[1]).reduce(
    (prev, current) => prev + current
  );
  const cx2 = p2.map((p) => p[0]).reduce(
    (prev, current) => prev + current
  );
  const cy2 = p2.map((p) => p[1]).reduce(
    (prev, current) => prev + current
  );

  const dist = Math.sqrt((cx1-cx2)^2 + (cy1-cy2^2));
  return (p1.length + p2.length)/(Math.log(dist));
};

function calcSiinIndex(t1, t2) {
  calcObject = {};
  for (const [key, value] of Object.entries(t1)) {
    calcObject[key] = [value, 0];
  }
  for (const [key, value] of Object.entries(t2)) {
    if (key in calcObject) {
      calcObject[key][1] = value;
    } else { calcObject[key] = [0, value] }
  }
  const sum = Object.values(calcObject)
    .map((v) => v[0]+v[1])
    .reduce((prev, curr) => prev + curr);
  const diff = Object.values(calcObject)
    .map((v) => Math.abs(v[0]-v[1]))
    .reduce((prev, curr) => prev + curr);
  return (sum-diff)/sum;
};

celeryWorker.register("tasks.calcDindinIndex", (pingId, sidi, siin) => {
  let query = {_id: pingId };
  let dataToUpdate= { "dindin": sidi*siin }
  let options = {useFindAndModify: false}
  Ping.findOneAndUpdate(query, dataToUpdate, options, (err, document) => {
    if (err) return err;
    console.log(document);
  }
)
  return sidi*siin;
});

celeryWorker.start();

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
