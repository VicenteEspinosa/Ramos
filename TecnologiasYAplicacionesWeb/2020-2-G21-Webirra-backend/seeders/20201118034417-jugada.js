'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const jugadas_array = [];

    jugadas_array.push({
      id: 1,
      ataques_jugador1: '{}',
      reordenamientos_jugador1: '{}',
      ataques_jugador2: '{}',
      reordenamientos_jugador2: '{}',
      ataques_jugador3: '{}',
      reordenamientos_jugador3: '{}',
      numero_jugada: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
      partidaId: 0
    });

    return queryInterface.bulkInsert('jugadas', jugadas_array);
    /**
     * Add seed commands here.
     *   numero_jugada, "createdAt", "updatedAt", "partidaId")

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
