const distancia = 11
const maxX = 7.32 / 2 /*3.66*/
const maxZ = 2.44
const numeroDePelotas = 5

const densidad = 1
const area = 0.039
const masa = 0.45
const D = 0.22
const g = 9.81

const v = getCookie('vInicialFutbol')
const vAngular = getCookie('vAgularFutbol')
const phi = getCookie('phiFutbol')
const theta = getCookie('thetaFutbol')

const Cd = 0.3
const Cl = 0.1
const Cs0 = 0.25
const ms = 0.8
const Kd = 0.013
const Kl = 0 /*0.004*/

const Sp0 = 0.1875


function crearPelota(x, y, z) {
    let img = document.createElement("img");
    img.src = "../img/futbol.png";
    img.className = "pelota"
    let porcentaje = 5 - (y / distancia) * 3.5

    img.style.height = `${porcentaje}%`
    img.style.width = `${porcentaje}%`
    img.style.left = `${36 + (x + maxX) * 2.2}%`
    img.style.top = `${80 - (z / maxZ) * 22}%`

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

final = tiempoFinal()

for (let i = numeroDePelotas - 1; i > -1; i--){ 
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
    let xFinal = X(final)
    let zFinal = Z(final)
    let fallo = true
    if ( Math.abs(xFinal) <= maxX && zFinal < maxZ) {
        fallo = false
    }
    return fallo
}

function error(){
    let error = 0
    if (X(final) < 0 && Math.abs(X(final)) > maxX) {
        error = x(final) + maxX
    }
    else if (Math.abs(X(final)) > maxX) {
        error = X(final) - maxX
    }
    if (Z(final) > maxZ) {
        error = error * error + (Z(final) - maxZ) * (Z(final) - maxZ)
    }
    return error
}

var resultado = document.getElementById('resultado')
if (fallo()) {
    console.log("FALLO")
    resultado.appendChild(document.createTextNode('FALLASTE POR ' + error() + ' METROS'))
    resultado.style.background = 'red';
}
else {
    console.log("GOL")
    resultado.appendChild(document.createTextNode('GOL'))
    resultado.style.background = '#3acf27';
}

console.log(Y(tiempoFinal()))
console.log(X(2))
console.log(Z(2))
console.log(tiempoFinal())