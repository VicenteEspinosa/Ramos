const { Model } = require('sequelize');

module.exports = (sequelize, DataTypes) => {
    class Order extends Model {

    }
    Order.init({
        /* id: {
          type: DataTypes.INTEGER,
          primaryKey: true,
        }, */
        internalid: DataTypes.STRING,
        cliente: DataTypes.STRING,
        sku: DataTypes.INTEGER,
        fechaentrega: DataTypes.DATE,
        cantidad: DataTypes.INTEGER,
        urlnotification: DataTypes.STRING,
        state: DataTypes.STRING,
        canal: DataTypes.STRING
    }, {
        sequelize,
        modelName: 'Order',
    });
    return Order;
};