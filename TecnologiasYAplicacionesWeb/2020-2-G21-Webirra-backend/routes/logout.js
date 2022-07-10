const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
require('dotenv').config();
const customerAuth = require('../middlewares/auth');
const jwt = require('jsonwebtoken');
const { json } = require('sequelize');
const router = new koaRouter()
const TOKEN_SECRET = process.env.TOKEN_SECRET;



router.post('logout', '/', customerAuth, async (ctx) => {
  console.log("")
    console.log("/logout")
    console.log("")

    const body = await ctx.request.body;
    const bcrypt = await require('bcrypt');

    const token = body["token"]

    const user = await ctx.db.jugador.findOne({where: {"token": token} })


    if (user){
        await user.update({ token: '' });
        ctx.body = {
          "status": "success",
          "msg": "Has cerrado sesion"
        };
        console.log('logout exitoso')

    }
    else{
      ctx.body = {
        "status": "error",
        "msg": "No has iniciado sesión"
      };
    }

});

module.exports = router;
