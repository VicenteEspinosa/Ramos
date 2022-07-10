'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const zonas = await queryInterface.sequelize.query(`SELECT id FROM public.zonas`);
    const zonas_ids = zonas[0];

    const misions_array = [];

    misions_array.push({
      objetivo: 'Conquistar Sur_este',
      id: 0,
      zonaId: zonas_ids[0].id,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    misions_array.push({
      objetivo: 'Conquistar Sur_oeste',
      id: 1,
      zonaId: zonas_ids[1].id,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    misions_array.push({
      objetivo: 'Conquistar Este',
      id: 2,
      zonaId: zonas_ids[2].id,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    misions_array.push({
      objetivo: 'Conquistar Oeste',
      id: 3,
      zonaId: zonas_ids[3].id,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    misions_array.push({
      objetivo: 'Conquistar Norte',
      id: 4,
      zonaId: zonas_ids[4].id,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    return queryInterface.bulkInsert('misions', misions_array);

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
