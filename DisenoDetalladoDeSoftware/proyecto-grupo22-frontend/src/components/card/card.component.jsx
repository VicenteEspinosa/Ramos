import React, { Component } from 'react';
import './card.styles.css';
import { formatCurrency, getUser } from '../../utils';

class Card extends Component {
  addItemToCart(event) {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/cart_items`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
       "product_id": event.target.id,
       "quantity": 1,
       "user_id": getUser().id
      })
    });
    event.preventDefault();
  }
  render() {
    return (
      <div className='card-container'>
        <h3 className='category'>{this.props.item.attributes.category}</h3>
        <img
          className='item-image'
          alt='item'
          src={this.props.item.attributes.image}
        />
        <div className='item-data-container'>
          <div className='item-name-container'>
            <h2>{this.props.item.attributes.name}</h2>
            <h3>Marca: {this.props.item.attributes.brand}</h3>
          </div>
          <p className='price'> {formatCurrency(this.props.item.attributes.price, this.props.dolar, this.props.dolarValue)} </p>
        </div>
        {this.props.route === 'Home' ? 
          <button
            id={this.props.item.attributes.id}
            onClick={this.addItemToCart}>
              Añadir al carrito
          </button> :
          <button>Editar Producto</button>
        }
      </div>
    )
  }
};

export default Card;
