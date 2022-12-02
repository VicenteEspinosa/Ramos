import Product from "./product";
import { useAppContext } from "./stateWrapper";

import style from "../styles/shoppingCart.module.css";

export default function ShoppingCart() {
  const cart = useAppContext();

  function getTotal() {
    const total = cart.items.reduce((acc, item) => {
      return (acc += item.qty * item.price);
    }, 0);
    return total;
  }

  function handleClickClose() {
    cart.closeCart();
  }

  return (
    <div
      className={style.shoppingCart}
      style={{ display: cart.isOpen ? "block" : "none" }}
    >
      <button onClick={handleClickClose} className={style.close}>
        Cerrar
      </button>

      {cart.items.length === 0 ? (
        <div className={style.empty}>No hay eventos que comprar</div>
      ) : (
        <>
          <h3>Tus eventos</h3>
          <div className={style.items}>
            {cart.items &&
              cart.items.length > 0 &&
              cart.items.map((item, i) => (
                <Product
                  key={item + i.toString()}
                  item={item}
                  showAs="ListItem"
                  qty={item.qty}
                />
              ))}
          </div>
          <div className={style.total}>Total: ${getTotal()}k</div>
        </>
      )}
    </div>
  );
}
