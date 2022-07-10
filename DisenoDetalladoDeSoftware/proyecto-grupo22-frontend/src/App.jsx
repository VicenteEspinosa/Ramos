import React, { Component } from 'react';
import { CardGrid } from './components/cardGrid/cardGrid.component';
import { NavBar } from './components/navbar/navbar.component';
import { SearchBox } from './components/searchBox/searchBox.component';
import './App.css';
import Login from '../src/routes/login';
import { getUser } from "./utils";

function setUser(user) {
  sessionStorage.setItem('user', JSON.stringify(user));
}

class App extends Component {
  constructor() {
    super();

    this.state = {
      products: [],
      searchField: '',
      dolar: false,
      dolarValue: this.getDolar(),
      isSignedIn: false
    };
  }

  componentDidMount() {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/products`)
      .then(response => response.json())
      .then(products => this.setState({ products: products.data }));
  }

  onSearchChange = event => {
    this.setState({ searchField: event.target.value });
  };

  onRouteChange = (route) => {
    if (route === 'home') {
      this.setState({ isSignedIn: true })
    }
    this.setState({ route: route })
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
    const { products, searchField, dolar, dolarValue, isSignedIn } = this.state;
    const filteredItems = products.filter(product =>
      product.attributes.name.toLowerCase().includes(searchField.toLowerCase()) +
      product.attributes.brand.toLowerCase().includes(searchField.toLowerCase()) +
      product.attributes.category.toLowerCase().includes(searchField.toLowerCase())
    );

    if(!isSignedIn) {
      return <Login setUser={setUser} onRouteChange={this.onRouteChange} />
    }

    return (
      <div className='App'>
        <NavBar route='Home' username={getUser().full_name} />
        <SearchBox onSearchChange={this.onSearchChange} />
        <button className="dolar" onClick={this.clickDolar}>Cambiar a 
          {dolar ? " pesos" : " dolar"}</button>
        <div className='app-items-container'>
          <CardGrid dolar={dolar} dolarValue={dolarValue} items={filteredItems} route='Home'/>
        </div>
      </div>
    );
  }
}

export default App;
