const { storeClient } = require('../services/mainServer')
const { generateHash } = require('../utils/cryptoHelpers')

async function moveItem(req, res) {
  try {
    let authHash;
    authHash = generateHash('GET');
    const stores = await storeClient.get('/almacenes', {headers: {
      'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
    }});

    const storageIds = {};

    for (const store of stores.data) {
      if (store.recepcion) storageIds['recepcion'] = store._id;
      if (store.despacho) storageIds['despacho'] = store._id;
      if (store.pulmon) storageIds['pulmon'] = store._id;
      if (store.cocina) storageIds['cocina'] = store._id;
      if (!store.recepcion && !store.despacho && !store.pulmon && !store.cocina) storageIds['general'] = store._id;
    }

    authHash = generateHash(`POST${req.body.productoId}${storageIds[req.body.storage]}`);
    const storeResponse = await storeClient.post('moveStock',{ productoId: req.body.productoId, almacenId: storageIds[req.body.storage]},{
    headers: {
      'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`,
      'Content-Type': 'application/json'
    },
    });

    return res.status(200).send(storeResponse.data);
  } catch (error) {
    console.log(error.message);
    
    return res.status(500).send(error);
  }
}

module.exports = {
  moveItem,
};
