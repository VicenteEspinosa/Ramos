const { factoryClient, storeClient } = require('../services/mainServer')
const { generateHash } = require('../utils/cryptoHelpers')
const jsonData = require('../utils/productos.json');

async function requestItem(req, res) {
  try {
    let authHash;
    authHash = generateHash(`PUT${req.body.sku}${req.body.cantidad}`);
    const factoryResponse = await factoryClient.put('fabricarSinPago',req.body,{
    headers: {
      'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`,
      'Content-Type': 'application/json'
    },
    });

    return res.status(200).send(factoryResponse.data);
  } catch (error) {
    console.log('LINEA 18 - FACTORY.CONTROLLER');
    console.log(error.message);
    return res.status(500).send(error.message);
  }
}

async function moveStockBodega(req, res){
  const data = req.body;
  try {
    let authHash;
    authHash = generateHash(`POST${data.productoId}${data.almacenId}`);
    const bodegaResponse = await storeClient.post('moveStockBodega', data, {
      headers:{
        'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`,
        'Content-Type': 'application/json'
      }
    });
    return res.status(200).send(bodegaResponse.data);
  } catch (err){
    return res.status(400).send({
      message: err.message
    })
  }
} 

module.exports = {
  requestItem,
  moveStockBodega
};
