const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const router = new koaRouter();


router.post('/', async (ctx) => {
    console.log("")
    console.log("/register")
    console.log("")

    const body = await ctx.request.body;


    console.log(body)
    const bcrypt = await require('bcrypt');
    const saltRounds = 10;

    const mail = body["mail"]
    const user = body["username"]
    const password = await body["password"]

    console.log("===========================================================")

    const salt = await bcrypt.genSaltSync(saltRounds)
    console.log({'salt': salt})
    console.log({'pass': password})
    console.log({'user': user})

    const hash = bcrypt.hashSync(password, salt)
    let creado = await ctx.db.jugador.findOne({where: {"mail": mail} })
    if (creado === null){
        console.log({"username": user, "password": hash, "mail": mail, "token": null})
        let mensaje_a_enviar = {"status": "success", "username": user, "password": hash, "mail": mail, "token": null}
        ctx.body = mensaje_a_enviar
        await ctx.db.jugador.create({"username": user, "password": hash, "mail": mail, "token": null})
        let jugador_nuevo = await ctx.db.jugador.findAll({limit: 1, order: [['createdAt', 'DESC']]})
        await ctx.db.estadistica.create({"partidas": 0, "victorias": 0, "tropas_perdidas": 0, "ataques_totales": 0, "ataques_exitosos": 0, "ataques_fallidos": 0, "jugadorId": jugador_nuevo[0].id})
    }
    else {
        console.log("Este mail ya ha sido usado")
        let mensaje_a_enviar = {"status": "error", "msg": "Ya existe un usuario con ese mail"}
        // Dar mensaje de error
        ctx.body = mensaje_a_enviar
    }
    console.log("===========================================================")

 })

 module.exports = router;
