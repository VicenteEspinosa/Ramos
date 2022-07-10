import React from 'react';

import './searchBox.styles.css';

export const SearchBox = props => (
  <div className='container'>
    <input
      className='search-box'
      type='search'
      placeholder='Buscar items por Nombre, Marca o Categoría'
      onChange={props.onSearchChange}
    />
  </div>
);