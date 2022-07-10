const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const customerAuth = require('../middlewares/auth');
const router = new koaRouter()


router.get('/',  async (ctx) => {
    console.log("")
    console.log("/crear")
    console.log("")

    const base = require("../data/base.json");
    const ultima_jugada = await ctx.db.jugada.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    const ultima_partida = await ctx.db.partida.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    for (let j = 0; j < 20; j++){
        let tropas = Math.floor(Math.random() * 10) + 1
        let propietario = Math.floor(Math.random() * 3) + 1
        base["territorios"][j]["id_jugador"] = propietario
        base["territorios"][j]["tropas"] = tropas
    }

    console.log("Nuevo mapa:" +  base)

    await ctx.db.partida.create({"estado": "creando", "id_jugador1": null, "id_jugador2": null, "id_jugador2": null}) // CREAR PARTIDA
    await ctx.db.jugada.create({"id": ultima_jugada[0].id + 1, "ataques_jugador1": '{}', "reordenamientos_jugador1": '{}', "ataques_jugador2": '{}', "reordenamientos_jugador2": '{}', "ataques_jugador3": '{}', "reordenamientos_jugador3": '{}', "numero_jugada": 1, "partidaId": ultima_partida[0].id + 1}) //CREAR TURNO

    await ctx.db.estado.create({"numero_jugada": 0, "territorios": JSON.stringify(base["territorios"]), "porcentaje_mision_jugador1": 0, "porcentaje_mision_jugador2": 0, "porcentaje_mision_jugador3": 0, "partidaId": ultima_partida[0].id + 1}) // CREAR MAPA
    ctx.body = base
    ultima_partida[0].estado = "terminada"
    ultima_partida[0].save()
})


module.exports = router;
