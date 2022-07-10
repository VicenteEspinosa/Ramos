import "./Cupons.css";
import dummyData from "../../dummyDataCupons";
import Cupon from "../Cupon/Cupon";

function Cupons() {
  return (
    <div className="Cupons">
      <div className="Title">Cupones Usados</div>
      <div className="Cupons-list">
        {dummyData.map((cupon, index) => (
          <Cupon
            className="Cupon"
            key={index}
            name={cupon.name}
            description={cupon.description}
            categories={cupon.categories}
            saved={cupon.saved}
          />
        ))}
      </div>
    </div>
  );
}

export default Cupons;
