import React, { Component } from 'react';
import './categoryCreate.styles.css';

class CategoryCreate extends Component {
  constructor() {
    super();
    this.state = { value: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value })
  }
  handleSubmit(event) {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/categories`, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({
       "name": this.state.value
      })
    });
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit} className='box'>
        <h2>Crear Nueva Categoría</h2>
        <label className='input-create'>
          Nombre:
          <input type="text" value={this.state.value} onChange={this.handleChange} placeholder='Nombre Categoría' />
        </label>
        <input type="submit" value="Guardar" className='save' />
      </form>
    );
  }
}

export default CategoryCreate;
