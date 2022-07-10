import { useState } from "react";
import "./cartDetail.scss"
import { useNavigate } from "react-router-dom";
import { RiCoupon2Line } from 'react-icons/ri';
import { formatCurrency, getUser } from "../../utils";


export function CartDetail(props) {
  const { products, total, coupon, dolar, dolarValue } = props;
  const [localCoupon, setLocalCoupon] = useState(coupon);
  const [percentage, setPercentage] = useState(0.1);
  const [couponInput, setCouponInput] = useState("");
  const tip = Math.round(total * percentage);

  const handleChange = (e) => {
    const newPercentage = e.target.value;
    setPercentage(newPercentage);
  };
  const navigate = useNavigate();

  const addCoupon = (coupon_id) => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/shopping_carts/-1`, {
      method: 'PUT',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
          user_id: getUser().id,
          coupon_id: coupon_id
      })})
  }


  const validateCoupon = () => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/coupons/verify`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
       "code": couponInput
      })})
      .then(res => res.json())
      .then(data => {
        if (Object.keys(data).includes("coupon_id")) {
          setLocalCoupon({name: couponInput, value: data.value});
          addCoupon(data.coupon_id);
        } else {
          alert("Coupon invalido");
        }
      })
  }

  const payCart = (e) => {
    const productList = products.map(product => ({ id: product.product.id, quantity: product.quantity }));
    const data = {
      "data": {
        "products": productList,
        "total": total + tip + 3500
      }
    };
    const requestOptions = {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    };

    fetch(`${process.env.REACT_APP_BACKEND_URL}/pay_cart/${getUser().id}`, requestOptions)
        .then(response => response.json())
        .then(data => navigate("/"))
  };

  return (
    <div className="product-detail">
      <table>
        <thead>
          <th></th>
          <th></th>
        </thead>
        <tbody>
          <tr>
            <td>Total productos</td>
            <td> {formatCurrency(total, dolar, dolarValue)}</td>
          </tr>
          <tr>
            <td>Costo de envío</td>
            <td> {formatCurrency(3500, dolar, dolarValue)}</td>
          </tr>
          <tr>
            <td>Descuento</td>
            {localCoupon ? <td>-{formatCurrency(localCoupon.value, dolar, dolarValue)}</td> : <td>$ 0</td>}
          </tr>
          <tr>
            <td>Propina</td>
            
              <td>
                <div className="options">
                  <div>
                    {formatCurrency(tip, dolar, dolarValue)}
                  </div>
                  <div>
                    <select value={percentage} onChange={handleChange}>
                    <option value={0}>0</option>
                      <option value={0.05}>5%</option>
                      <option value={0.1}>10%</option>
                      <option value={0.15}>15%</option>
                      <option value={0.2}>20%</option>
                    </select>
                  </div>
                </div>
              </td>
            
          </tr>
          <tr>
            <td>Costo final</td>
            <td>{formatCurrency(total + tip + 3500 - (localCoupon ? localCoupon.value : 0), dolar, dolarValue)}</td>
          </tr>
        </tbody>
      </table>
        {localCoupon ? <div className="coupon"><RiCoupon2Line/> {localCoupon.name}</div> :
        <div className="addCoupon">
          <input
            className="couponInput"
            type={"text"}
            placeholder={"Ingresar Cupón"}
            onChange={e => {setCouponInput(e.target.value)}}>  
          </input>
          <button className="couponButton" onClick={validateCoupon}>Validar</button>
        </div>
      }
      <button onClick={payCart}>Pagar</button>
    </div>
  );
}