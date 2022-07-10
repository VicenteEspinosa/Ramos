'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class jugada extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  jugada.init({
    ataques_jugador1: DataTypes.STRING,
    reordenamientos_jugador1: DataTypes.STRING,
    ataques_jugador2: DataTypes.STRING,
    reordenamientos_jugador2: DataTypes.STRING,
    ataques_jugador3: DataTypes.STRING,
    reordenamientos_jugador3: DataTypes.STRING,
    numero_jugada: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'jugada',
  });
  return jugada;
};