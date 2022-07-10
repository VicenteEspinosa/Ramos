const { storeClient } = require('../services/mainServer')
const { generateHash } = require('../utils/cryptoHelpers')


async function get_stock() {
  let authHash;
  authHash = generateHash('GET');
  const stores = await storeClient.get('/almacenes', {headers: {
    'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`
  }});

  const stock = {};

  for (const store of stores.data) {
    authHash = generateHash(`GET${store._id}`);
    const availableSKUSResponse = await storeClient.get('/skusWithStock', {
      params: {
        almacenId: store._id,
      },
      headers: {
        'Authorization': `${process.env.BASE_AUTH_TOKEN}${authHash}`,
      }
    })
    const availableItems = availableSKUSResponse.data;
    for (const item of availableItems) {
      if (!stock[item._id]) {
        stock[item._id] = item.total;
      } else {
        stock[item._id] += item.total;
      }
    };
  }
  return stock;
}

async function get(req, res) {
  try {
    const stock = await get_stock();

    return res.status(200).send(Object.keys(stock).map(key => {
      return {'sku': key, 'stock': stock[key]}
    }));
  } catch (error) {
    console.log(error.message);
    
    return res.status(500).send(error);
  }
}

module.exports = {
  get,
  get_stock,
};
