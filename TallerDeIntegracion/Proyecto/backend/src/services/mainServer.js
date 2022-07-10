const axios = require('axios');
const dotenv = require('dotenv');
dotenv.config()

const storeClient = axios.create({
  baseURL: process.env.STORE_URL,
  timeout: 1000,
  raxConfig: {
    retry: 3,
    retryDelay: 4000
  }
});

const factoryClient = axios.create({
  baseURL: process.env.FACTORY_URL,
  timeout: 1000,
  raxConfig: {
    retry: 3,
    retryDelay: 4000
  }
});

const ocClient = axios.create({
  baseURL: process.env.OC_URL,
  timeout: 1000,
});

module.exports = {
  storeClient,
  factoryClient,
  ocClient,
}
