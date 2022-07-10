const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const customerAuth = require('../middlewares/auth');
const router = new koaRouter()


router.get('/'  ,async (ctx) => {
    console.log("")
    console.log("/estadisticas")
    console.log("")


    const stats = await ctx.db.estadistica.findAll()
    /* Entrega todas las estadisticas ordenadas de mayor a menor, y con el nombre */
    var partidas = [] /* [ [nombre, partidas], [nombre2, partidas2] ]*/
    var victorias = []
    var tropas_perdidas = []
    var ataques_totales = []
    var ataques_exitosos = []
    var ataques_fallidos = []

    for (let i = 0; i < stats.length; i++){
        let usuario = await ctx.db.jugador.findOne({where: {"id": stats[i].jugadorId} })
        let nombre = usuario.username
        
        /* PARTIDAS */
        if (partidas.length > 0){
            let noEntro = true
            for (let j = 0; j < partidas.length; j++){
                if (noEntro){
                    if (stats[i].partidas > partidas[j][1]){
                        partidas.splice(j, 0, [nombre, stats[i].partidas])
                        noEntro = false        
                    }
                }
                
            }
            if (noEntro) {
                partidas.push([nombre, stats[i].partidas])
            }
        }
        else {
            partidas.push([nombre, stats[i].partidas])
        }

      /* VICTORIAS */
        if (victorias.length > 0){
            let noEntro = true
            for (let j = 0; j < victorias.length; j++){
                if (noEntro){
                    if (stats[i].victorias > victorias[j][1]){
                        victorias.splice(j, 0, [nombre, stats[i].victorias])
                        noEntro = false        
                    }
                }
                
            }
            if (noEntro) {
                victorias.push([nombre, stats[i].victorias])
            }
        }
        else {
            victorias.push([nombre, stats[i].victorias])
        }

        /* TROPAS PERDIDAS */
        if (tropas_perdidas.length > 0){
            let noEntro = true
            for (let j = 0; j < tropas_perdidas.length; j++){
                if (noEntro){
                    if (stats[i].tropas_perdidas > tropas_perdidas[j][1]){
                        tropas_perdidas.splice(j, 0, [nombre, stats[i].tropas_perdidas])
                        noEntro = false        
                    }
                }
                
            }
            if (noEntro) {
                tropas_perdidas.push([nombre, stats[i].tropas_perdidas])
            }
        }
        else {
            tropas_perdidas.push([nombre, stats[i].tropas_perdidas])
        }

        /* ATAQUES TOTALES */
        if (ataques_totales.length > 0){
            let noEntro = true
            for (let j = 0; j < ataques_totales.length; j++){
                if (noEntro){
                    if (stats[i].ataques_totales > ataques_totales[j][1]){
                        ataques_totales.splice(j, 0, [nombre, stats[i].ataques_totales])
                        noEntro = false        
                    }
                }
                
            }
            if (noEntro) {
                ataques_totales.push([nombre, stats[i].ataques_totales])
            }
        }
        else {
            ataques_totales.push([nombre, stats[i].ataques_totales])
        }


        /* ATAQUES EXITOSOS */
        if (ataques_exitosos.length > 0){
            let noEntro = true
            for (let j = 0; j < ataques_exitosos.length; j++){
                if (noEntro){
                    if (stats[i].ataques_exitosos > ataques_exitosos[j][1]){
                        ataques_exitosos.splice(j, 0, [nombre, stats[i].ataques_exitosos])
                        noEntro = false        
                    }
                }
                
            }
            if (noEntro) {
                ataques_exitosos.push([nombre, stats[i].ataques_exitosos])
            }
        }
        else {
            ataques_exitosos.push([nombre, stats[i].ataques_exitosos])
        }

        /* ATAQUES FALLIDOS */
        if (ataques_fallidos.length > 0){
            let noEntro = true
            for (let j = 0; j < ataques_fallidos.length; j++){
                if (noEntro){
                    if (stats[i].ataques_fallidos > ataques_fallidos[j][1]){
                        ataques_fallidos.splice(j, 0, [nombre, stats[i].ataques_fallidos])
                        noEntro = false        
                    }
                }
                
            }
            if (noEntro) {
                ataques_fallidos.push([nombre, stats[i].ataques_fallidos])
            }
        }
        else {
            ataques_fallidos.push([nombre, stats[i].ataques_fallidos])
        }
    }


    ctx.body = {
        "partidas": partidas,
        "victorias": victorias,
        "tropas_perdidas": tropas_perdidas,
        "ataques_totales": ataques_totales,
        "ataques_exitosos": ataques_exitosos,
        "ataques_fallidos": ataques_fallidos
    }
    })

module.exports = router;
