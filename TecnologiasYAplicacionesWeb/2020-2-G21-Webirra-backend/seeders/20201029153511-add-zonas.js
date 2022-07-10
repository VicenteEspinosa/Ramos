'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const zonas_array = [];

    zonas_array.push({
      nombre: 'Sur_este',
      id: 0,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    zonas_array.push({
      nombre: 'Sur_oeste',
      id: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    zonas_array.push({
      nombre: 'Este',
      id: 2,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    zonas_array.push({
      nombre: 'Oeste',
      id: 3,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    zonas_array.push({
      nombre: 'Norte',
      id: 4,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    zonas_array.push({
      nombre: 'Centro',
      id: 5,
      createdAt: new Date(),
      updatedAt: new Date(),
    });

    return queryInterface.bulkInsert('zonas', zonas_array);
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
