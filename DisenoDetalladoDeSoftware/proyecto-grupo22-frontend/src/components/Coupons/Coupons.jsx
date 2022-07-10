import "./Coupons.styles.css";
import React, { Component } from "react";
import { Coupon } from "../Coupon/Coupon";
import { NavBar } from "../navbar/navbar.component";

function getUser() {
  const userString = sessionStorage.getItem('user');
  const user = JSON.parse(userString);
  return user
}

class Coupons extends Component {
  constructor() {
    super();

    this.state = {
      coupons: [],
      dolar: false,
      dolarValue: this.getDolar(),
    };
  }

  componentDidMount() {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/used_coupons`)
      .then((response) => response.json())
      .then((coupons) => this.setState({ coupons: coupons.data }));
  }
  clickDolar = () => {
    this.setState({ dolar: !this.state.dolar });
  }
  getDolar = () => {
    fetch('https://mindicador.cl/api/dolar')
      .then((response) => response.json())
      .then((dolarPrices) => this.setState({ dolarValue: dolarPrices.serie[0].valor }));
  }
  render() {
    const { coupons, dolar, dolarValue } = this.state;
    return (
      <div>
        <NavBar route='Coupons' username={getUser().full_name} />
        <div className="Coupons">
          <div className="Title">Cupones Usados</div>
          <button className="dolar" onClick={this.clickDolar}>Cambiar a 
          {dolar ? " pesos" : " dolar"}</button>
          <div className="Coupons-list">
            {coupons.map((coupon, index) => (
              <Coupon
                className="Coupon"
                key={index}
                dolar={dolar}
                dolarValue={dolarValue}
                name={coupon.attributes.name}
                description={coupon.description}
                category={coupon.attributes.category}
                saved={coupon.attributes.value}
              />
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default Coupons;
