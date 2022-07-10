import "./BoughtItem.css";
import { addDotsToNumber } from "../../utils";

function BoughtItem({ icon, name, units, price }) {
  return (
    <div className="BoughtItem">
      <div className="columnIcon">
        <img src={icon} className="BoughtItem-icon" alt="Icon"></img>
      </div>
      <div className="columnName">
        <div className="BoughtItem-name">{name}</div>
        <div className="BoughtItem-units">
          {units} {units > 1 ? " unidades" : " unidad"}
        </div>
      </div>
      <div className="columnPrice">
        <div className="BoughtItem-price">${addDotsToNumber(price)} /u</div>
      </div>
    </div>
  );
}

export default BoughtItem;
