
const KoaRouter = require('koa-router');

const login = require('./routes/login');
const register = require('./routes/register');
const jugada = require('./routes/jugada');
const crear = require('./routes/crear');
const estado_tablero = require('./routes/estado_tablero');
const jugar = require('./routes/jugar');
const logout = require('./routes/logout');
const estado_partida = require('./routes/estado_partida');
const estadisticas = require('./routes/estadisticas');


const router = new KoaRouter();

router.use('/login', login.routes());
router.use('/register', register.routes());
router.use('/jugada', jugada.routes());
router.use('/crear', crear.routes());
router.use('/estado_tablero', estado_tablero.routes());
router.use('/jugar', jugar.routes());
router.use('/logout', logout.routes());
router.use('/estado_partida', estado_partida.routes());
router.use('/estadisticas', estadisticas.routes());

module.exports = router;
