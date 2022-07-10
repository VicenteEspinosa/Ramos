'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('estadisticas', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      partidas: {
        type: Sequelize.INTEGER
      },
      victorias: {
        type: Sequelize.INTEGER
      },
      tropas_perdidas: {
        type: Sequelize.INTEGER
      },
      ataques_totales: {
        type: Sequelize.INTEGER
      },
      ataques_exitosos: {
        type: Sequelize.INTEGER
      },
      ataques_fallidos: {
        type: Sequelize.INTEGER
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('estadisticas');
  }
};
