vInicialMax = 1000
vAngularMax = 100
phiMax = 360
thetaMax = 360  
/*
Ks =0
*/

function actualizarInputs() {
    let vInicial = document.getElementById('vInicial').value
    let vAngular = document.getElementById('vAngular').value
    let phi = document.getElementById('phi').value
    let theta = document.getElementById('theta').value
    
    /* Revisar si inputs validos */

    console.log("vInicial anterior: " + getCookie('vInicialTenis'))
    console.log("vAngular anterior: " + getCookie('vAngularTenis'))
    console.log("phi anterior: " + getCookie('phiTenis'))
    console.log("thetha anterior: " + getCookie('thetaTenis'))
    
    console.log("vInicial nueva: " + vInicial)
    console.log("vAngular nueva: " + vAngular)
    console.log("phi nueva: " + phi)
    console.log("theta nueva: " + theta)

    createCookie('vInicialTenis', vInicial, 1)
    createCookie('vAngularTenis', vAngular, 1)
    createCookie('phiTenis', phi, 1)
    createCookie('thetaTenis', theta, 1)
    
    console.log("")
    window.location.replace("canchaTenis.html");
}

function recibirInputs() {
    document.getElementById('vInicial').style.borderColor = '#ffffff'
    document.getElementById('vAngular').style.borderColor = "#ffffff"
    document.getElementById('phi').style.borderColor = "#ffffff"
    document.getElementById('theta').style.borderColor = "#ffffff"

    let vInicial = document.getElementById('vInicial').value
    let vAngular = document.getElementById('vAngular').value
    let phi = document.getElementById('phi').value
    let theta = document.getElementById('theta').value
    var correcto = true
    if (vInicial <= 0 || vInicial > vInicialMax || vInicial == undefined || vInicial == '') {
        correcto = false
        document.getElementById('vInicial').style.borderColor = "red"
        console.log("Error en velocidad incial")
    }
    if (vAngular <= 0 || vAngular > vAngularMax || vAngular == undefined || vAngular == '') {
        correcto = false
        document.getElementById('vAngular').style.borderColor = "red"
        console.log("Error en velocidad angular")
    }
    if (phi < 0 || phi > phiMax || phi == undefined || phi == '') {
        correcto = false
        document.getElementById('phi').style.borderColor = "red"
        console.log("Error en phi")
    }
    if (theta < 0 || theta > thetaMax || theta == undefined || theta == '') {
        correcto = false
        document.getElementById('theta').style.borderColor = "red"
        console.log("Error en theta")
    }
 
    if (correcto) {
        console.log("correcto")
        actualizarInputs()
    }
    else {
        alert("Por favor revisa tus inputs")
    }
}