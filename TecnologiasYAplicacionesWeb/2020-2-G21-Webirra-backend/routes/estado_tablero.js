const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const customerAuth = require('../middlewares/auth');
const estadistica = require('../models/estadistica');
const router = new koaRouter()


router.get('/', customerAuth,  async (ctx) => {
    console.log("")
    console.log("/estado_tablero")
    console.log("")

    var estado = await ctx.db.estado.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    var partida = await ctx.db.partida.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    const territorios = await JSON.parse(estado[0].territorios);
    const numero_jugada = await JSON.parse(estado[0].numero_jugada);
    const numero_partida = await JSON.parse(estado[0].partidaId);
    var jugador1 = ""
    var jugador2 = ""
    var jugador3 = ""
    const id1 = partida[0].id_jugador1
    const id2 = partida[0].id_jugador2
    const id3 = partida[0].id_jugador3
    if (id1 === undefined) {
        jugador1 = null
    }
    else {
        jugador1 = await ctx.db.jugador.findOne({where: {"id": id1} })
    }

    if (id2 === undefined) {
        jugador2 = null
    }
    else {
        jugador2 = await ctx.db.jugador.findOne({where: {"id": id2} })
    }

    if (id3 === undefined) {
        jugador3 = null
    }
    else {
        jugador3 = await ctx.db.jugador.findOne({where: {"id": id3} })
    }


    var msg = {}
    msg["territorios"] = territorios
    msg["numero_jugada"] = numero_jugada
    if (jugador1 === null) {
        msg["nombre1"] = null
    }
    else {
        msg["nombre1"] = jugador1["username"]
    }
    if (jugador2 === null) {
        msg["nombre2"] = null
    }
    else {
        msg["nombre2"] = jugador2["username"]
    }
    if (jugador3 === null) {
        msg["nombre3"] = null
    }
    else {
        msg["nombre3"] = jugador3["username"]
    }
    const idMision1 = jugador1["misionId"]
    const idMision2 = jugador2["misionId"]
    const idMision3 = jugador3["misionId"]


    const mision1 = await ctx.db.mision.findOne({where: {"id": idMision1} })
    const mision2 = await ctx.db.mision.findOne({where: {"id": idMision2} })
    const mision3 = await ctx.db.mision.findOne({where: {"id": idMision3} })

    msg["mision1"] = mision1["objetivo"]
    msg["mision2"] = mision2["objetivo"]
    msg["mision3"] = mision3["objetivo"]

    msg["porcentaje_mision1"] = await calcular_porcentaje_mision(ctx, 1, territorios, mision1)
    msg["porcentaje_mision2"] = await calcular_porcentaje_mision(ctx, 2, territorios, mision2)
    msg["porcentaje_mision3"] = await calcular_porcentaje_mision(ctx, 3, territorios, mision3)

    msg["partidaId"] = numero_partida
    ctx.body = msg
    })

module.exports = router;


async function calcular_porcentaje_mision(ctx, id_jugador, territorios, mision){
    const id_zona_a_conquistar = mision["zonaId"]
    const territorios_a_conquistar = await ctx.db.territorio.findAll({where: {"zonaId": id_zona_a_conquistar}, attributes: ["id"] })
    let conquistados = 0
    for (let i = 0; i < territorios_a_conquistar.length; i++){
        if ( territorios[territorios_a_conquistar[i]["id"]]["id_jugador"] == id_jugador ){
            conquistados = conquistados + 1
        }
    }
    console.log("a conquistar:" + JSON.stringify(territorios_a_conquistar))
    let porcentaje = ((conquistados / territorios_a_conquistar.length)*100)
    if (porcentaje == 100){
        let partida = await ctx.db.partida.findAll({limit: 1, order: [['createdAt', 'DESC']]})
        let id_real = 0
        if (id_jugador == 1){
            id_real = partida[0].id_jugador1
        }
        else if (id_jugador == 2){
            id_real = partida[0].id_jugador2
        }
        else {
            id_real = partida[0].id_jugador3
        }
        
        let estadistica = await ctx.db.estadistica.findOne({where: {"jugadorId": id_real} });
        estadistica.victorias = estadistica.victorias + 1;
        await estadistica.save();
    }
    return porcentaje
}
