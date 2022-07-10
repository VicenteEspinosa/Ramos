'use strict';

var session = require('koa-session');
const koa = require('koa');
const koaRouter = require('koa-router');
const koaBody = require('koa-body');
const routes = require('./routes');
const cors = require('@koa/cors');

require('dotenv').config();

const app = new koa()
const router = new koaRouter()

app.keys = ['Shh, its a secret!'];
app.use(session(app));  // Include the session middleware

const db = require('./models');

const PORT = process.env.PORT || 3000;


db.sequelize
  .authenticate()
  .then(() => {
    console.log('Connection to the database has been established successfully.');
    app.listen(PORT, (err) => {
      if (err) {
        return console.error('Failed to conect', err);
      }
      console.log(`Listening on port ${PORT}`);
      return app;
    });
  })
  .catch((err) => console.error('Unable to connect to the database:', err));

app.use(koaBody());
app.use(cors());
app.context.db = db
app.use(routes.routes())

router.get('/', async (ctx) => {
    var estado = await db.estado.findByPk(1);
    var territorios = await JSON.parse(estado.territorios);
    ctx.body = await territorios;
    var n = ctx.session.views || 0;
    ctx.session.views = ++n;
})



app.use(router.routes())


// psql -U postgres
// \c risk
// yarn sequelize model:create --name partida --attributes id_partida:integer,estado:boolean,fecha_inicio:string,id_jugadores:string,historial_jugadas:string
