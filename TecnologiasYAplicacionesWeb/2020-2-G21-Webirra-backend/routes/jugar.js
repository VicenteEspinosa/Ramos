// Para enviar las jugadas de usuario a servidor

const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const customerAuth = require('../middlewares/auth');
const router = new koaRouter()

//router.post('/', customerAuth, async (ctx) => {

router.post('/', customerAuth, async (ctx) => {
    console.log("")
    console.log("/jugar")
    console.log("")

    const body = await ctx.request.body;

    const id_juego = body["id_juego"];
    console.log("ID JUEGO: " + id_juego)
    const ataques = body["ataques"];
    const reordenamientos = body["reordenamientos"];
    const turno = body["numero_jugada"];
    const partidaId = body["partidaId"]

    const ultimo_estado = await ctx.db.estado.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    const turno_actual = await JSON.parse(ultimo_estado[0].numero_jugada) + 1;

    const jugadas = await ctx.db.jugada.findOne({where: {"numero_jugada": turno, "partidaId": partidaId} })
    console.log('partidaid: '+ partidaId)
    if (turno == turno_actual && id_juego <= 3 && id_juego >=1 && ataques != undefined && reordenamientos != undefined) {
        ctx.body = await {
            'estado': "Success"
        }
        if (id_juego == 1) {
            console.log("Registrada jugada jugador 1")
            jugadas.ataques_jugador1 = await JSON.stringify(ataques)
            jugadas.reordenamientos_jugador1 = await JSON.stringify(reordenamientos)
        }
        else if (id_juego == 2) {
            console.log("Registrada jugada jugador 2")
            jugadas.ataques_jugador2 = await JSON.stringify(ataques)
            jugadas.reordenamientos_jugador2 = await JSON.stringify(reordenamientos)
        }
        else if (id_juego == 3) {
            console.log("Registrada jugada jugador 3")
            jugadas.ataques_jugador3 = await JSON.stringify(ataques)
            jugadas.reordenamientos_jugador3 = await JSON.stringify(reordenamientos)
        }
        await jugadas.save()
    }
    else {
        ctx.body = await {
            'estado': "Error",
            "input": body
        }
    }
})

module.exports = router;
