'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class partida extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      models.partida.hasMany(models.jugador);
      models.partida.hasMany(models.jugada);
      models.partida.hasMany(models.estado);
      // define association here
    }
  };
  partida.init({
    estado: DataTypes.STRING,
    fecha_inicio: DataTypes.STRING,
    id_jugador1: DataTypes.INTEGER,
    id_jugador2: DataTypes.INTEGER,
    id_jugador3: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'partida',
  });
  return partida;
};
