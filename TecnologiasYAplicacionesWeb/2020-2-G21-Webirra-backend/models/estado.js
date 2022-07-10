'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class estado extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  estado.init({
    numero_jugada: DataTypes.INTEGER,
    territorios: DataTypes.STRING,
    porcentaje_mision_jugador1: DataTypes.INTEGER,
    porcentaje_mision_jugador2: DataTypes.INTEGER,
    porcentaje_mision_jugador3: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'estado',
  });
  return estado;
};