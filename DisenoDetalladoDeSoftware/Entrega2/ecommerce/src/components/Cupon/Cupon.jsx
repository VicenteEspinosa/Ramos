import "./Cupon.css";
import { addDotsToNumber } from "../../utils";

function Cupon({ name, description, categories, saved }) {
  return (
    <div className="Cupon">
      <div className="column">
        <div className="Cupon-name">{name}</div>
        <div className="Cupon-description">{description}</div>
      </div>
      <div className="column">
        <div className="cuponCategories">
          {categories.map((category, index) => (
            <div
              className="Cupon-category"
              key={index}
              style={{ background: category[1] }}
            >
              {category[0]}
            </div>
          ))}
        </div>
      </div>
      <div className="column">
        <div className="Cupon-saved">Ahorrado: ${addDotsToNumber(saved)}</div>
      </div>
    </div>
  );
}

export default Cupon;
