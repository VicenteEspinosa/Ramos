import { useState } from "react";
import "./list.scss"
import { totalUtils, formatCurrency } from "../../utils";

export function ProductList(props) {
  const { products, total, setTotal, dolar, dolarValue } = props;
  const [cartProducts, setCartProducts] = useState(products);

  cartProducts.sort(function (a, b) {
    if (a.nombre > b.nombre) { return 1 }
    if (a.nombre < b.nombre) { return -1 }
    return 0;
  });

  function updateQuantity(itemId, quantity) {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/cart_items/${itemId}`, {
      method: 'PUT',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
       "quantity": quantity
      })
    });
  }

  function removeItem(itemId) {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/cart_items/${itemId}`, {
      method: 'DELETE',
    });
  }

  const handleClickUp = (e) => {
    const change = e.target.name;
    let newProducts = [...cartProducts];
    newProducts[change].quantity += 1;
    updateQuantity(newProducts[change].id, newProducts[change].quantity);
    const totalNew = totalUtils(cartProducts);
    setTotal(totalNew);
    setCartProducts(newProducts);
  };

  const handleClickDown = (e) => {
    const change = e.target.name;
    let newProducts = [...products];
    newProducts[change].quantity -= 1;
    if (newProducts[change].quantity === 0){
      removeItem(newProducts[change].id);
      newProducts.splice(change, 1);
    } else {
      updateQuantity(newProducts[change].id, newProducts[change].quantity);
    }
    const totalNew = totalUtils(cartProducts);
    setTotal(totalNew);
    setCartProducts(newProducts);
  };
  
  return (
    <div className="general">
      <table>
        <thead>
          <th>Ítem</th>
          <th>Descripción</th>
          <th>Precio unitario</th>
          <th>Cantidad</th>
          <th>Precio total</th>
        </thead>
        <tbody>
          {cartProducts.map((product, index) => (
            <tr key={index}>
              <td>
              <img src={product.product.image} alt="imagen"></img>
              </td>
              <td>{product.product.name} {product.product.brand}</td>
              <td>{formatCurrency(product.product.price, dolar, dolarValue)}</td>
              <td>
                <div className="columnInput">
                  <div className="cantidad">
                    x{product.quantity}
                  </div>
                  <div className="botonesCantidad">
                    <div>
                      <input type="button" onClick={handleClickUp} name={index} value="+"></input>
                    </div>
                    <div>
                      <input type="button" onClick={handleClickDown} name={index} value="-"></input> 
                    </div>
                  </div>
                </div>
              </td>
              <td>{formatCurrency(product.product.price * product.quantity, dolar, dolarValue)}</td>
            </tr>
          ))}
          <tr>
            <td></td>
            <td></td>
            <td></td>
            <td>Total:</td>
            <td>
              {formatCurrency(total, dolar, dolarValue)}
              </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}