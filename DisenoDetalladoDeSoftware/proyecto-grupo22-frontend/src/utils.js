const addDotsToNumber = (number) => {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
const totalUtils = (products) => {
    return products.map(product => product.product.price * product.quantity).reduce((prev, curr) => prev + curr, 0);
}
const toDolar = (oringinalValue, dolar) => {
    return addDotsToNumber((oringinalValue / dolar).toFixed(2));
}
const formatCurrency = (value, dolar, dolarValue) => {
    if (dolar) {
        return `$${toDolar(value, dolarValue)} USD`;
    }
    return `$${addDotsToNumber(value)} CLP`;
}

function getUser() {
    const userString = sessionStorage.getItem('user');
    const user = JSON.parse(userString);
    return user
  }

export { addDotsToNumber, totalUtils, toDolar, formatCurrency, getUser };