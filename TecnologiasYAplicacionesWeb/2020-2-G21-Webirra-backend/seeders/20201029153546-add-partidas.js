'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const partidas_array = [];

    partidas_array.push({
      id: 0,
      estado: 'creando',
      fecha_inicio: new Date(),
      createdAt: new Date(),
      updatedAt: new Date()
    });

    return queryInterface.bulkInsert('partidas', partidas_array);
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
    */
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  }
};
