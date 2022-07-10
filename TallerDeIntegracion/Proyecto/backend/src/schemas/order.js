const Joi = require('joi');

const orderSchema = Joi.object({
  internalid: Joi.string(),
  client: Joi.string(),
  sku: Joi.number(),
  fechaentrega: Joi.date(),
  cantidad: Joi.number(),
  urlnotificacion: Joi.string(),
  state: Joi.string(),
  canal: Joi.string()
});

/* const editorderSchema = Joi.object({
  username: Joi.string(),
  age: Joi.number(),
  psu_score: Joi.number(),
  university: Joi.string(),
  gpa_score: Joi.number(),
  job: Joi.string(),
  salary: Joi.number(),
  promotion: Joi.boolean(),
  hospital: Joi.string(),
  operations: Joi.array(),
  medical_debt: Joi.number(),
}); */

module.exports = {
  orderSchema
};
