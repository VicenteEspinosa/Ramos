import "./Purchases.styles.css";
import { Purchase } from "../Purchase/Purchase";
import React, { Component } from "react";
import { NavBar } from "../navbar/navbar.component";
import { getUser } from "../../utils";

class Purchases extends Component {
  constructor() {
    super();

    this.state = {
      purchases: [],
      dolar: false,
      dolarValue: this.getDolar(),
    };
  }
  componentDidMount() {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/shopping_history/${getUser().id}`)
      .then((response) => response.json())
      .then((purchases) => this.setState({ purchases: purchases.data }));
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
    const { purchases, dolar, dolarValue } = this.state;
    return (
      <div>
        <NavBar route="Purchases" username={getUser().full_name} />
        <button className="dolar" onClick={this.clickDolar}>Cambiar a 
          {dolar ? " pesos" : " dolar"}</button>
        <div className="Purchases">
          {purchases.map((purchase, index) => (
            <Purchase
              dolar={dolar}
              dolarValue={dolarValue}
              key={index}
              date={purchase.attributes.paymentDate}
              items={purchase.attributes.items}
              total={purchase.attributes.totalAmount}
              coupon={purchase.attributes.coupon}
              discount={purchase.attributes.discount}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default Purchases;
