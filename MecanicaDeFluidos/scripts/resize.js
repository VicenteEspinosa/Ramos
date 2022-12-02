function ajustarPantalla(){
    let ancho = window.screen.width
    let alto = window.screen.height

    let diferencia = Math.sqrt((ancho * ancho) + (alto * alto))/ Math.sqrt((864*864) + (1536 * 1536))
    let porcentaje = diferencia*100

    let ventana = document.getElementsByTagName("body")[0]
    ventana.setAttribute("style", `zoom: ${porcentaje}%` )
}

ajustarPantalla()

window.addEventListener('resize', ajustarPantalla)