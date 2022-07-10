'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('jugadas', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      ataques_jugador1: {
        type: Sequelize.STRING
      },
      reordenamientos_jugador1: {
        type: Sequelize.STRING
      },
      ataques_jugador2: {
        type: Sequelize.STRING
      },
      reordenamientos_jugador2: {
        type: Sequelize.STRING
      },
      ataques_jugador3: {
        type: Sequelize.STRING
      },
      reordenamientos_jugador3: {
        type: Sequelize.STRING
      },
      numero_jugada: {
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
    await queryInterface.dropTable('jugadas');
  }
};
