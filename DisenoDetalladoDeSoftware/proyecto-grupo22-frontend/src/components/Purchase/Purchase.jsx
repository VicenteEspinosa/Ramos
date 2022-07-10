import "./Purchase.styles.css";
import { BoughtItem } from "../BoughtItem/BoughtItem";
import { formatCurrency } from "../../utils";

export const Purchase = (props) => {
  return (
    <div className="Purchase">
      <div className="purchaseDate">{props.date}</div>
      <div className="columns">
        <div className="purchaseItems">
          {props.items.map((item, index) => (
            <BoughtItem
              dolar={props.dolar}
              dolarValue={props.dolarValue}
              key={index}
              icon={item.icon}
              name={item.name}
              units={item.quantity}
              price={item.price}
            />
          ))}
        </div>
        <div className="buttonsPricing">
          <div className="buttons">
            <div className="seeButtonHolder">
              <button className="seeButton">Ver compra</button>
            </div>
            <div className="buyAgainButtonHolder">
              <button className="buyAgainButton">Volver a comprar</button>
            </div>
          </div>
          <div className="purchasePricing">
            {props.coupon && props.discount ? (
              <div className="Puchase-cuponData">
                <div className="Puchase-pricing-subtotal">
                  Subtotal:{" "}
                  <div className="Puchase-pricing-subtotal-value">
                    {formatCurrency(props.total, props.dolar, props.dolarValue)}
                  </div>
                </div>
                <div className="Puchase-pricing-discount">
                  Cupón {props.coupon}:
                  <div className="Puchase-pricing-discount-value">
                    -{formatCurrency(props.discount, props.dolar, props.dolarValue)}
                  </div>
                </div>
              </div>
            ) : null}
            <div className="Puchase-pricing-total">
              Total: {formatCurrency(props.total - props.discount, props.dolar, props.dolarValue)}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
