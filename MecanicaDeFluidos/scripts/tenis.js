const distancia = 23.78 /* 11.89 *2 */
const maxX = 8.23
const minZ = 1.07
const numeroDePelotas = 5

const densidad = 1
const area = 0.0141
const masa = 0.0577
const D = 0.067
const g = 9.81

const v = getCookie('vInicialTenis')
const vAngular = getCookie('vAgularTenis')
const phi = getCookie('phiTenis')
const theta = getCookie('thetaTenis')

const Cd = 0.3
const Cl = 0.1
const Cs0 = 0.25
const ms = 0.8
const Kd = 0.013
const Kl = 0 /*0.004*/

const Sp0 = 0.1875

function crearPelota(x, y, z) {
    let img = document.createElement("img");
    img.src = "../img/tenis.png";
    img.className = "pelota"
    let porcentaje = 2

    img.style.height = `${porcentaje}%`
    img.style.width = `${porcentaje}%`
    img.style.left = `${10 + (y / distancia) * 68}%`
    img.style.top = `${80 - (z / minZ) * 7.5}%`

    var body = document.getElementsByTagName("body")[0];
    body.appendChild(img);
}

const Wz = phi * Math.cos(theta) * Math.cos(phi) + theta * Math.sin(phi)
const vy = Math.sin(theta) * Math.sin(phi) * v
const Sp = (D * vAngular) / (2 * v)
var Cs = 0 /* Despues se cambia */

if (Sp > 0.3) {
    Cs = Cs0 * (1 + ms/Cs0 * (0.3 - Sp0))
}
else {
    Cs = Cs0 * (1 + ms/Cs0 * (Sp - Sp0))
}

const ks = densidad * area * Cs / (2 * masa)

function X(t) {
    let primero = Kd * vy - (g*g*t*t - 4*g*Wz*t + 6*Wz*Wz) / (6*vy*vy)
    return (ks*v*v*t*t/2 * (1 - primero))
}

function Y(t) {
    return (v*t * (1 - (Kd*v*t) / 2))
}

function Z(t) {
    let primero = (Kd*g*v*t*t*t/6) - (Kd*Wz + Kl*v) * (v*t*t/2)
    if ((Wz*t - (g*t*t/2) + primero) < 0) {
        return 0
    }
    return (Wz*t - (g*t*t/2) + primero)
}


function tiempoFinal() {
    let opcion1 = (v - Math.sqrt( v*v *(-2*distancia*Kd + 1) )) / (Kd * v*v)
    let opcion2 = (v + Math.sqrt( v*v *(-2*distancia*Kd + 1) )) / (Kd * v*v)
    if ( Math.abs( Y(opcion1) - distancia) < Math.abs( Y(opcion2) - distancia)) {
        return opcion1
    }
    else {
        return opcion2
    }
}

function tiempoMalla() {
    let opcion1 = (v - Math.sqrt( v*v *(-distancia*Kd + 1) )) / (Kd * v*v)
    let opcion2 = (v + Math.sqrt( v*v *(-distancia*Kd + 1) )) / (Kd * v*v)
    if ( Math.abs( Y(opcion1) - distancia/2) < Math.abs( Y(opcion2) - distancia/2)) {
        return opcion1    
    }
    else {
        return opcion2
    }
}

function tiempoPiso() { /* Creo que la formula esta mal */
    let opcion1 = (v - Math.sqrt( v*v *(1) )) / (Kd * v*v)
    let opcion2 = (v + Math.sqrt( v*v *(1) )) / (Kd * v*v)
    if ( Math.abs( Z(opcion1)) < Math.abs( Z(opcion2))) {
        return opcion1    
    }
    else {
        return opcion2
    }
}


var final = tiempoFinal()
var estado = "no malla"
if (Z(tiempoMalla()) < minZ) {
    /* CHOCO EN LA RED */
    final = tiempoMalla()
    estado = "malla"
}

/*
for (let i = numeroDePelotas - 1; i > -1; i--){ */
for (let i = 0; i < numeroDePelotas; i++){
    x = X(final * i / (numeroDePelotas - 1))
    y = Y(final * i / (numeroDePelotas - 1))
    z = Z(final * i / (numeroDePelotas - 1))
    console.log("x: " + x)
    console.log("y: " + y)
    console.log("z: " + z)
    console.log("")
    crearPelota(x, y, z)
}


function fallo() {
    let yFinal = Y(tiempoPiso())
    let fallo = true
    if ( yFinal <= distancia) {
        fallo = false
    }
    return fallo
}
var resultado = document.getElementById('resultado')
if (estado == 'no malla') {
    if (fallo()) {
        console.log("FALLO")
        resultado.appendChild(document.createTextNode('FALLASTE'))
        resultado.style.background = 'red';
    }
    else {
        console.log("BUEN SAQUE!")
        resultado.appendChild(document.createTextNode('BUEN SAQUE!'))
        resultado.style.background = '#3acf27';
    }
}
else {
    console.log("MALLA")
    resultado.appendChild(document.createTextNode('CHOCÓ EN LA RED'))
    resultado.style.background = 'red'; 
}

console.log(Y(tiempoFinal()))
console.log(X(2))
console.log(Z(2))
console.log(tiempoFinal())
