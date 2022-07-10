import "./Purchase.css";
import BoughtItem from "../BoughtItem/BoughtItem";
import { addDotsToNumber } from "../../utils";

function Purchase({ date, items, total, cupon, discount }) {
  return (
    <div className="Purchase">
      <div className="purchaseDate">{date}</div>
      <div className="columns">
        <div className="purchaseItems">
          {items.map((item, index) => (
            <BoughtItem
              key={index}
              icon={item.icon}
              name={item.name}
              units={item.units}
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
            {cupon && discount ? (
              <div className="Puchase-cuponData">
                <div className="Puchase-pricing-subtotal">
                  Subtotal:{" "}
                  <div className="Puchase-pricing-subtotal-value">
                    ${addDotsToNumber(total + discount)}
                  </div>
                </div>
                <div className="Puchase-pricing-discount">
                  Cupón {cupon}:
                  <div className="Puchase-pricing-discount-value">
                    -${addDotsToNumber(discount)}
                  </div>
                </div>
              </div>
            ) : null}
            <div className="Puchase-pricing-total">
              Total: ${addDotsToNumber(total)}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Purchase;
