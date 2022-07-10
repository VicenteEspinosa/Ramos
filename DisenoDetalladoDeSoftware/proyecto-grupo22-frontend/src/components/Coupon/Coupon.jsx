import "./Coupon.styles.css";
import { addDotsToNumber } from "../../utils";
import { toDolar } from "../../utils";

export const Coupon = (props) => {
  return (
    <div className="Coupon">
      <div className="column">
        <div className="Coupon-name">{props.name}</div>
        <div className="Coupon-description">{props.description}</div>
      </div>
      <div className="column">
        <div className="couponCategories">
          <div
            className="Coupon-category"
            style={{ background: "blue" }}
          >
            {props.category}
          </div>
        </div>
      </div>
      <div className="column">
        <div className="Coupon-saved">
          Ahorrado: 
          {props.dolar ? (toDolar(props.saved, props.dolarValue) + " USD") :
          addDotsToNumber(props.saved) + " CLP"}
        </div>
      </div>
    </div>
  );
};
