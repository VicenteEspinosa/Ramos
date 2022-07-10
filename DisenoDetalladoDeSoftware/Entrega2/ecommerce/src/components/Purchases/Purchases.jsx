import './Purchases.css';
import Purchase from '../Purchase/Purchase';
import dummyData from '../../dummyData';

function Purchases() {
  return (
    <div className="Purchases">
        {dummyData.map((purchase, index) => (
            <Purchase key={index}
            date={purchase.date}
            items={purchase.items}
            total={purchase.total}
            cupon={purchase.cupon}
            discount={purchase.discount}
            />
        ))}
    </div>
  );
}

export default Purchases;
