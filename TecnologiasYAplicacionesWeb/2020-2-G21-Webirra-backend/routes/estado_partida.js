const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const customerAuth = require('../middlewares/auth');
const router = new koaRouter()


//Recibe id del usuario
router.post('/', customerAuth,  async (ctx) => {
    console.log("")
    console.log("/estado_partida")
    console.log("")

    const body = await ctx.request.body;

    var partida = await ctx.db.partida.findAll({limit: 1, order: [['createdAt', 'DESC']]})

    var estado = await partida[0].estado;
    var usuario1 = await partida[0].id_jugador1
    var usuario2 = await partida[0].id_jugador2
    var usuario3 = await partida[0].id_jugador3
    var id_juego = null
    
    if (usuario1 === undefined) {
        usuario1 = null
    }
    if (usuario2 === undefined) {
        usuario2 = null
    }
    if (usuario3 === undefined) {
        usuario3 = null
    }

    var estado_usuario = ""
    if (body["id"] == usuario1 || body["id"] == usuario2 || body["id"] == usuario3) {
        if (usuario3 != null) {
            estado_usuario = "Listo"
        }
        else {
            estado_usuario = "Unido esperando"
        }

        if (body["id"] == usuario1) {
            id_juego = 1
        }
        else if (body["id"] == usuario2) {
            id_juego = 2
        }
        else {
            console.log("USUARIO2: " + usuario2)
            id_juego = 3
        }
    }
    else if (usuario3 === null) {
        if (usuario2 === null){
            if (usuario1 === null){
                usuario1 = body["id"]
                partida[0].id_jugador1 = body["id"]
                estado_usuario = "Se unio"
                await asignar_mision(ctx, body["id"], partida[0])
                id_juego = 1
            }
            else {
                usuario2 = body["id"]
                partida[0].id_jugador2 = body["id"]
                estado_usuario = "Se unio"
                await asignar_mision(ctx, body["id"], partida[0])
                id_juego = 2
            }
        }
        else {
            usuario3 = body["id"]
            partida[0].id_jugador3 = body["id"]
            estado_usuario = "Se unio, listo"
            await asignar_mision(ctx, body["id"], partida[0]) //Por que si es el jugador 3 entonces ya se lleno el juego
            id_juego = 3
            partida[0].estado = "jugando" // Empezar partida
            let date = new Date()
            partida[0].fecha_inicio = date.toString()
        }
        await partida[0].save()

        var estadisticas = await ctx.db.estadistica.findOne({where: {"jugadorId": body["id"]} })
        estadisticas.partidas = estadisticas.partidas + 1;
        estadisticas.save()
    }
    else {
        estado_usuario = "Lleno"
    }
    console.log("")
    console.log("Consulta hecha por usuario numero " + id_juego)
    console.log("")
    var msg = {
        "estado": estado,
        "id1": usuario1,
        "id2": usuario2,
        "id3": usuario3,
        "estado_usuario": estado_usuario,
        "id_juego": id_juego
    }
    ctx.body = msg
    })


async function asignar_mision(ctx, id_jugador, partida){
    const aleatorio = Math.floor(Math.random() * 4) 
    const mision = await ctx.db.mision.findByPk(aleatorio)
    var jugador = await ctx.db.jugador.findOne({where: {"id": id_jugador}})
    jugador.misionId = mision["id"]
    jugador.partidaId = partida.id
    jugador.save()
}


module.exports = router;
