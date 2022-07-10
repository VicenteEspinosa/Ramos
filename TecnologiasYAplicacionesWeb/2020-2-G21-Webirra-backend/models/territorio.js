'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class territorio extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      models.territorio.belongsToMany(models.territorio, { through: 'vecinos', as: 'Vecinos' });
      // define association here
    }
  };
  territorio.init({
    nombre: DataTypes.STRING,
    n_tropas: DataTypes.INTEGER,
  }, {
    sequelize,
    modelName: 'territorio',
  });
  return territorio;
};
