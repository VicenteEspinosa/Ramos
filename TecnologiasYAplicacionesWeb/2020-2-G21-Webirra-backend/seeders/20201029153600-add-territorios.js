'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    const zonas = await queryInterface.sequelize.query(`SELECT id FROM public.zonas`);
    const zonas_ids = zonas[0];


    const territorios_array = [];
    territorios_array.push({
      nombre: 'Ingenieria',
      id: 0,
      zonaId: zonas_ids[0].id,
      n_tropas: 5,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Construccion_civil',
      id: 1,
      zonaId: zonas_ids[0].id,
      n_tropas: 3,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Enfermeria',
      id: 2,
      zonaId: zonas_ids[0].id,
      n_tropas: 2,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Luksic',
      id: 3,
      zonaId: zonas_ids[0].id,
      n_tropas: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Educacion',
      id: 4,
      zonaId: zonas_ids[1].id,
      n_tropas: 3,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Humanidades',
      id: 5,
      zonaId: zonas_ids[1].id,
      n_tropas: 2,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Hall',
      id: 6,
      zonaId: zonas_ids[1].id,
      n_tropas: 5,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'College',
      id: 7,
      zonaId: zonas_ids[2].id,
      n_tropas: 3,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Salud',
      id: 8,
      zonaId: zonas_ids[2].id,
      n_tropas: 5,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Matematicas',
      id: 9,
      zonaId: zonas_ids[2].id,
      n_tropas: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Fisica_quimica',
      id: 10,
      zonaId: zonas_ids[2].id,
      n_tropas: 2,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Comercial',
      id: 11,
      zonaId: zonas_ids[3].id,
      n_tropas: 3,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Capilla',
      id: 12,
      zonaId: zonas_ids[5].id,
      n_tropas: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Sociales',
      id: 13,
      zonaId: zonas_ids[3].id,
      n_tropas: 2,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Agronomia',
      id: 14,
      zonaId: zonas_ids[3].id,
      n_tropas: 5,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Aula_magna',
      id: 15,
      zonaId: zonas_ids[3].id,
      n_tropas: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Cancha_futbol',
      id: 16,
      zonaId: zonas_ids[4].id,
      n_tropas: 3,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Gimnasio',
      id: 17,
      zonaId: zonas_ids[4].id,
      n_tropas: 5,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Cancha_basketball',
      id: 18,
      zonaId: zonas_ids[4].id,
      n_tropas: 2,
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    territorios_array.push({
      nombre: 'Cancha_tenis',
      id: 19,
      zonaId: zonas_ids[4].id,
      n_tropas: 1,
      createdAt: new Date(),
      updatedAt: new Date(),
    });

    return queryInterface.bulkInsert('territorios', territorios_array);


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
