const {
  Model,
} = require('sequelize');

module.exports = (sequelize, DataTypes) => {
  class User extends Model {

    static associate(models) {
      this.hasMany(models.AccessTokenRequest, { onDelete: 'cascade' });
    }
  }
  User.init({
    username: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true,
    },
    password: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    name: DataTypes.STRING,
    age: DataTypes.INTEGER,
    psu_score: DataTypes.INTEGER,
    university: DataTypes.STRING,
    gpa_score: DataTypes.FLOAT,
    job: DataTypes.STRING,
    salary: DataTypes.FLOAT,
    promotion: DataTypes.BOOLEAN,
    hospital: DataTypes.STRING,
    operations: DataTypes.ARRAY(DataTypes.STRING),
    medical_debt: DataTypes.FLOAT,
  }, {
    sequelize,
    modelName: 'User',
  });
  return User;
};
