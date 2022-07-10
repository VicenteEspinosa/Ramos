import "./BoughtItem.styles.css";
import { formatCurrency } from "../../utils";

export const BoughtItem = props => {
  return (
    <div className="BoughtItem">
      <div className="columnIcon">
        <img src={props.icon} className="BoughtItem-icon" alt="Icon"></img>
      </div>
      <div className="columnName">
        <div className="BoughtItem-name">{props.name}</div>
        <div className="BoughtItem-units">
          {props.units} {props.units > 1 ? " unidades" : " unidad"}
        </div>
      </div>
      <div className="columnPrice">
        <div className="BoughtItem-price">{formatCurrency(props.price, props.dolar, props.dolarValue)} /u</div>
      </div>
    </div>
  );
}