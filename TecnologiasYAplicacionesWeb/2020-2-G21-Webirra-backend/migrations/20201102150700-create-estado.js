'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('estados', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      numero_jugada: {
        type: Sequelize.INTEGER
      },
      territorios: {
        type: Sequelize.TEXT
      },
      porcentaje_mision_jugador1: {
        type: Sequelize.INTEGER
      },
      porcentaje_mision_jugador2: {
        type: Sequelize.INTEGER
      },
      porcentaje_mision_jugador3: {
        type: Sequelize.INTEGER
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('estados');
  }
};
