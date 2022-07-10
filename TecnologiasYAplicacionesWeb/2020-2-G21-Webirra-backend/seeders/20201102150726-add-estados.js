'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    return queryInterface.bulkInsert('estados', [
  {
    numero_jugada: 0,
    territorios: JSON.stringify({"0": {"id_jugador": 1, "tropas": 10}, "1": {"id_jugador": 3, "tropas": 7},
    "2": {"id_jugador": 1, "tropas": 10}, "3": {"id_jugador": 2, "tropas": 6}, "4": {"id_jugador": 3, "tropas": 12}
    , "5": {"id_jugador": 1, "tropas": 17}, "6": {"id_jugador": 1, "tropas": 5}, "7": {"id_jugador": 1, "tropas": 4}
    , "8": {"id_jugador": 1, "tropas": 9}, "9": {"id_jugador": 2, "tropas": 8}, "10": {"id_jugador": 2, "tropas": 7},
    "11": {"id_jugador": 1, "tropas": 4}, "12": {"id_jugador": 3, "tropas": 6}, "13": {"id_jugador": 2, "tropas": 13},
    "14": {"id_jugador": 2, "tropas": 7}, "15": {"id_jugador": 2, "tropas": 8}, "16": {"id_jugador": 3, "tropas": 2},
    "17": {"id_jugador": 3, "tropas": 7}, "18": {"id_jugador": 2, "tropas": 10}, "19": {"id_jugador": 1, "tropas": 4}}),
    porcentaje_mision_jugador1: 0,
    porcentaje_mision_jugador2: 0,
    porcentaje_mision_jugador3: 0,
    createdAt: new Date(),
    updatedAt: new Date(),
    partidaId: 0
  }]);
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
