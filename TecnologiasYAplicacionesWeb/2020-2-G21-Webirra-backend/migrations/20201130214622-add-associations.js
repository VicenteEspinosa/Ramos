'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    return queryInterface.addColumn(
      'jugadors', // name of Source model
      'partidaId', // name of the key we're adding
      {
        type: Sequelize.INTEGER,
        references: {
          model: 'partidas', // name of Target model
          key: 'id', // key in Target model that we're referencing
        },
        onUpdate: 'CASCADE',
        onDelete: 'SET NULL',
      }
    ).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'territorios', // name of Target model
        'jugadorId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'jugadors', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'jugadors', // name of Target model
        'misionId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'misions', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'territorios', // name of Target model
        'zonaId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'zonas', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'jugadas', // name of Target model
        'partidaId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'partidas', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'misions', // name of Target model
        'zonaId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'zonas', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'estados', // name of Target model
        'partidaId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'partidas', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      // Order hasMany Product
      return queryInterface.addColumn(
        'estadisticas', // name of Target model
        'jugadorId', // name of the key we're adding
        {
          type: Sequelize.INTEGER,
          references: {
            model: 'jugadors', // name of Source model
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        }
      );
    }).then(() => {
      return queryInterface.createTable('vecinos', {
        idTerritorio1: {
          type: Sequelize.INTEGER,
          references: {
            model: 'territorios',
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',
        },
        idTerritorio2: {
          type: Sequelize.INTEGER,
          references: {
            model: 'territorios',
            key: 'id',
          },
          onUpdate: 'CASCADE',
          onDelete: 'SET NULL',

        }
      })
    });
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
  }
};
