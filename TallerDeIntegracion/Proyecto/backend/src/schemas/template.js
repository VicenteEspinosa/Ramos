const Joi = require('joi');

const userSchema = Joi.object({
  username: Joi.string()
    .required(),
  name: Joi.string(),
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
  password: Joi.string()
    .required(),
});

const editUserSchema = Joi.object({
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
});

module.exports = {
  userSchema,
  editUserSchema,
};
