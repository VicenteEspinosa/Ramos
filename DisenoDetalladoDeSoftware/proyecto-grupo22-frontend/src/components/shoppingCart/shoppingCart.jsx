import { useState, useEffect } from "react";
import { ProductList } from "../productList/productList";
import { CartDetail } from "../cartDetail/cartDetail"
import { NavBar } from "../navbar/navbar.component"
import  Map  from "../../img/map.png"
import "./cart.scss"
import { totalUtils, getUser } from "../../utils";

export function ShoppingCart() {
  const [products, setProducts] = useState([]);
  const [coupon, setCoupon] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [total, setTotal] = useState(0);
  const [dolar, setDolar] = useState(false);
  const [dolarValue, setDolarValue] = useState(0);


  function clickDolar () {
    setDolar(!dolar);
  }

  function getDolarValue () {
    fetch('https://mindicador.cl/api/dolar')
      .then((response) => response.json())
      .then((dolarPrices) =>  setDolarValue(dolarPrices.serie[0].valor));
  }

  getDolarValue();


  useEffect(() => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/shopping_carts/${getUser().id}`)
      .then((response) => response.json())
      .then((product) => {
        setProducts(product?.data);
        setCoupon(product?.coupon);
        setIsLoading(false);
        const sTotal = totalUtils(product["data"]);
        setTotal(sTotal);
      });
  }, [isLoading]);
  if (isLoading) {
    return (
      <div>
      <NavBar username={getUser().full_name}></NavBar>
      
      <div className="columns">
        Cargando...
      </div>
    </div>
    )
  }
  
  return (
    <div>
      <NavBar username={getUser().full_name}></NavBar>
      <div className="dolarButtonContainer">
        <button className="dolar" onClick={clickDolar}>Cambiar a {dolar ? " pesos" : " dolares"}</button>
      </div>
      <div className="columns">
        <div className="left">
          <ProductList
            dolarValue={dolarValue}
            dolar={dolar}
            products={products}
            total={total}
            setTotal={setTotal}/>
        </div>
        <div className="right">
          <div className="image">
            <img src={Map} alt="ubicación"></img>
          </div>
          <CartDetail
            dolarValue={dolarValue}
            dolar={dolar}
            total={total}
            products={products}
            coupon={coupon}/>
        </div>
      </div>
    </div>
  );
}
