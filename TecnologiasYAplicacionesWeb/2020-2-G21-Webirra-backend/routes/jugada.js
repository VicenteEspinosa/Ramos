const koaRouter = require('koa-router');
const bcrypt = require('bcrypt');
const customerAuth = require('../middlewares/auth');
const router = new koaRouter()


router.get('/', customerAuth,  async (ctx) => {
    console.log("")
    console.log("/jugada")
    console.log("")

    var estado = await ctx.db.estado.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    var estado_actual = await JSON.parse(estado[0].territorios);

    var porcentaje_1 = estado[0].porcentaje_mision_jugador1
    var porcentaje_2 = estado[0].porcentaje_mision_jugador2
    var porcentaje_3 = estado[0].porcentaje_mision_jugador3


    const ultimas_jugadas = await ctx.db.jugada.findAll({limit: 1, order: [['createdAt', 'DESC']]})
    respuesta1 = {}
    respuesta1["id_usuario"] = 1
    respuesta1["ataques"] = await JSON.parse(ultimas_jugadas[0]["dataValues"]["ataques_jugador1"])
    respuesta1["reordenamietos"] = await JSON.parse(ultimas_jugadas[0]["dataValues"]["reordenamientos_jugador1"])

    respuesta2 = {}
    respuesta2["id_usuario"] = 2
    respuesta2["ataques"] = await JSON.parse(ultimas_jugadas[0]["dataValues"]["ataques_jugador2"])
    respuesta2["reordenamietos"] = await JSON.parse(ultimas_jugadas[0]["dataValues"]["reordenamientos_jugador2"])

    respuesta3 = {}
    respuesta3["id_usuario"] = 3
    respuesta3["ataques"] = await JSON.parse(ultimas_jugadas[0]["dataValues"]["ataques_jugador3"])
    respuesta3["reordenamietos"] = await JSON.parse(ultimas_jugadas[0]["dataValues"]["reordenamientos_jugador3"])

    var hay_ataque1 = await JSON.stringify(respuesta1["ataques"]) != '{}'
    var hay_reordenamiento1 = await JSON.stringify(respuesta1["reordenamietos"]) != '{}'
    var jug_1_listo = await hay_ataque1 || hay_reordenamiento1

    var hay_ataque2 = await JSON.stringify(respuesta2["ataques"]) != '{}'
    var hay_reordenamiento2 = await JSON.stringify(respuesta2["reordenamietos"]) != '{}'
    var jug_2_listo = await hay_ataque2 || hay_reordenamiento2

    var hay_ataque3 = await JSON.stringify(respuesta3["ataques"]) != '{}'
    var hay_reordenamiento3 = await JSON.stringify(respuesta3["reordenamietos"]) != '{}'
    var jug_3_listo = await hay_ataque3 || hay_reordenamiento3
    console.log(JSON.stringify(respuesta1))
    console.log(JSON.stringify(respuesta2))
    console.log(JSON.stringify(respuesta3))


    var todos_listos = await jug_1_listo && jug_2_listo && jug_3_listo

    var fecha = await new Date (estado[0].createdAt.toJSON())
    var now = await new Date();
    var diferencia = await (now - fecha);
    var dif_mins = await Math.round(((diferencia % 86400000) % 3600000) / 60000);

    if (!todos_listos && dif_mins < 5){
      ctx.body = {"status": "error"}
    }

    else{
      const respuestas = [respuesta1, respuesta2, respuesta3]

      /* var estado_actual = "como estaba el mapa antes del turno (voy a ir editandolo pa mandar esta misma varible al final)" */

      var ataques = [] /* [[id_llega1, cantidad1, atacante1], [id_llega2, cantidad2, atacante2]] */
      var refuerzos = [] /* [[id_llega1, cantidad1], [id_llega2, cantidad2]] */
      var salidas = [] /* [[id_salio1, cantidad1], [id_salio2, cantidad2]] */


      var numero_jugada = estado[0].numero_jugada + 1


      for (let i = 0; i < respuestas.length; i++){ /* uno por usuario */
          let respuesta = respuestas[i]
          let usuario_actual = respuesta["id_usuario"]
          let usuario_ataques = respuesta["ataques"]
          let usuario_refuerzos = respuesta["reordenamientos"]

          if (usuario_ataques === undefined){
              usuario_ataques = []
          }
          if (usuario_refuerzos === undefined){
           usuario_refuerzos = []
       }

          for (let i = 0; i < usuario_ataques.length; i++){ /* uno por ataque*/
              let lista = []
              lista.push(usuario_ataques[i]["id_territorio_atacado"])
              lista.push(usuario_ataques[i]["tropas"])
              lista.push(usuario_actual)
              ataques.push(lista)

              let lista2 = []
              lista2.push(usuario_ataques[i]["id_territorio_saliente"])
              lista2.push(usuario_ataques[i]["tropas"])
              salidas.push(lista2)
          }

          for (let i = 0; i < usuario_refuerzos.length; i++){ /* uno por refuerzo*/
              let lista = []
              lista.push(usuario_refuerzos[i]["id_territorio_entrante"])
              lista.push(usuario_refuerzos[i]["tropas"])
              refuerzos.push(lista)

              let lista2 = []
              lista2.push(usuario_refuerzos[i]["id_territorio_saliente"])
              lista2.push(usuario_refuerzos[i]["tropas"])
              salidas.push(lista2)
          }
      }



      /*
      Reforzar lugares donde enviaron tropas
      */

      for (let i = 0; i < refuerzos.length; i++){
          estado_actual[refuerzos[i][0]]["tropas"] = estado_actual[refuerzos[i][0]]["tropas"] + refuerzos[i][1]
      }


      /*
      Sacar tropas de donde salieron
      */

      for (let i = 0; i < salidas.length; i++){
          estado_actual[salidas[i][0]]["tropas"] = estado_actual[salidas[i][0]]["tropas"] - salidas[i][1]
      }


      /*
      Ataques dobles
      */

      var ataques_al_mismo_lugar = [] /* listas con ataques repetidos */

      for (let i = 0; i < 20; i++){
          let lista = []
          for (let j = 0; j < ataques.length; j++){
              if (i == ataques[j][0]){
                  lista.push(ataques[j])
              }
         }
         if (lista.length > 1){ /* Se sacan ambos ataques repetidos de la lista ataques */
              ataques_al_mismo_lugar.push(lista)
              let index = ataques.indexOf(ataques_al_mismo_lugar[0])
              ataques.splice(index, 1)
              let index2 = ataques.indexOf(ataques_al_mismo_lugar[1])
              ataques.splice(index2, 1)

         }
      }


       async function Pelea(tropas1, tropas2, idJugador1, idJugador2, peleaPrevia){
           let tropasIniciales1 = tropas1
           let tropasIniciales2 = tropas2
           let ultima_partida = await ctx.db.partida.findAll({limit: 1, order: [['createdAt', 'DESC']]})
           let ids = [ultima_partida[0].id_jugador1, ultima_partida[0].id_jugador2, ultima_partida[0].id_jugador3]
           let jugador1 = ids[idJugador1 - 1]
           let jugador2 = ids[idJugador2 - 1]
           let estadisticas1 = await ctx.db.estadistica.findOne({where: {"jugadorId": jugador1} })
           let estadisticas2 = await ctx.db.estadistica.findOne({where: {"jugadorId": jugador2} })
           if (peleaPrevia == false) {
                   estadisticas1.ataques_totales = estadisticas1.ataques_totales + 1
                   estadisticas2.ataques_totales = estadisticas2.ataques_totales + 1
                   console.log("ATAQUES TOTALES " + estadisticas2.ataques_totales)
           }
           while (tropas1 > 0 && tropas2 > 0){
               let n1 = 0
               let n2 = 0

               for (let i = 0; i < tropas1; i++){
                   let numero = Math.floor(Math.random() * 10); /* Numero entre 0 y 9 */
                   if (numero > n1){
                       n1 = numero
                   }
               }

               for (let i = 0; i < tropas2; i++){
                   let numero = Math.floor(Math.random() * 10); /* Numero entre 0 y 9 */
                   if (numero > n2){
                       n2 = numero
                   }
               }

               if (n1 > n2){
                   tropas2--
               }
               else if (n2 < n1){
                   tropas2--
               }
           }
           /* Contar tropas perdidas*/
           estadisticas1.tropas_perdidas = estadisticas1.tropas_perdidas + tropasIniciales1 - tropas1
           estadisticas2.tropas_perdidas = estadisticas1.tropas_perdidas + tropasIniciales2 - tropas2

           console.log("TROPAS PERDIDAS" + estadisticas2.tropas_perdidas)
           if (tropas1 > 0){
                   estadisticas2.ataques_fallidos = estadisticas2.ataques_fallidos + 1
                   console.log("ATAQUES FALLIDOS " + estadisticas2.ataques_fallidos)
                   if (peleaPrevia) {
                       estadisticas2.ataques_totales = estadisticas2.ataques_totales + 1
                   }
                   else {
                       estadisticas1.ataques_exitosos = estadisticas1.ataques_exitosos + 1
                       console.log("ATAQUES EXITOSOS " + estadisticas2.ataques_exitosos)
                   }
                   await estadisticas1.save()
                   await estadisticas2.save()
                   return [0, tropas1]
           }
           else {
                   estadisticas1.ataques_fallidos = estadisticas1.ataques_fallidos + 1
                   if (peleaPrevia){
                       estadisticas1.ataques_totales = estadisticas1.ataques_totales + 1
                   }
                   else {
                       estadisticas2.ataques_exitosos = estadisticas2.ataques_exitosos + 1
                   }
                   await estadisticas1.save()
                   await estadisticas2.save()
                   return [1, tropas2]
               }
       }

      for (let j = 0; j < ataques_al_mismo_lugar.length; j++){ /* Resolver ataques al mismo lugar */
           let repetido = ataques_al_mismo_lugar[j]
           let resultado = await Pelea(repetido[0][1], repetido[1][1], repetido[0][2], repetido[1][2], true)
           console.log("RESULTADO: " + resultado)
           repetido[resultado[0]][1] = resultado[1] /* actualizar tropas restantes ganador */
           ataques.push(repetido[resultado[0]]) /* Se agrega el ganador a ataques, con las tropas sobrevivientes */
       }


      /*
      Resolver Ataques
      */


      for (let j = 0; j < ataques.length; j++){ /* Resolver ataques a territorios */
          let resultado = await Pelea(ataques[j][1], estado_actual[ataques[j][0]]["tropas"], ataques[j][2], estado_actual[ataques[j][0]]["id_jugador"], false ) /* Pelea entre atacante y defensor */
          /* actualizar tropas y dueño territorio */
          console.log('ataques[j]: ' + ataques[j])
          console.log('resultado: ' + resultado)
           if (resultado[0] == 0){ /* Gano defensa */
               estado_actual[ataques[j][0]]["tropas"] = resultado[1]
               console.log('ganoelquedefiende')
           }
           else if (resultado[0] == 1){
               estado_actual[ataques[j][0]]["tropas"] = resultado[1]
               estado_actual[ataques[j][0]]["id_jugador"] = ataques[j][2]
               console.log('gano el que ataca')
               console.log(ataques[j]) /* Cambiar dueño */
           }
      }


      var str_est = JSON.stringify(estado_actual)
      var ultima_partida = await ctx.db.partida.findAll({limit: 1, order: [['createdAt', 'DESC']]})

       await ctx.db.estado.create({"territorios": str_est, "numero_jugada": numero_jugada, "porcentaje_mision_jugador1": porcentaje_1, "porcentaje_mision_jugador2": porcentaje_2, "porcentaje_mision_jugador3": porcentaje_3, "partidaId": ultima_partida[0]["id"]})

       await ctx.db.jugada.create({"ataques_jugador1": '{}', "reordenamientos_jugador1": '{}', "ataques_jugador2": '{}', "reordenamientos_jugador2": '{}', "ataques_jugador3": '{}', "reordenamientos_jugador3": '{}', "numero_jugada": numero_jugada + 1, "partidaId": ultima_partida[0]["id"]})

       ctx.body = await estado_actual;
    }
})



module.exports = router;
