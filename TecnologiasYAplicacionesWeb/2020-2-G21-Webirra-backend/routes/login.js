const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
require('dotenv').config();
const customerAuth = require('../middlewares/auth');
const jwt = require('jsonwebtoken');
const { json } = require('sequelize');
const router = new koaRouter()
const TOKEN_SECRET = process.env.TOKEN_SECRET;



router.post('/',  async (ctx) => {
    console.log("")
    console.log("/login")
    console.log("")

    const body = await ctx.request.body;
    const bcrypt = await require('bcrypt');

    const mail = body["mail"]
    const password = body["password"]
    const token = jwt.sign({ mail }, TOKEN_SECRET);

    const user = await ctx.db.jugador.findOne({where: {"mail": mail} })


    if (user){
        const hash = user["dataValues"]["password"]
        const id = user["dataValues"]["id"]
        const res = bcrypt.compareSync(password, hash)
        console.log("===========================================================")
        if (res == true){
            await user.update({ token });
            console.log("Login exitoso, tu id es: " + id + ', token:' + token)
            ctx.body = {
                "status": "success",
                "id": id,
                "token": token
            }
        }
        else {
            console.log("Contraseña incorrecta!")
            ctx.body = {
                "status": "error",
                "msg": "Contraseña incorrecta"
            }
        }
        console.log("===========================================================")
    }
    else{
        console.log("No hay un usuario registrado con este mail")
        ctx.body = {
            "status": "error",
            "msg": "No hay un usuario registrado con ese mail"
        }
    }
    




});

module.exports = router;
