import React from 'react';
import Card from '../card/card.component';

import './cardGrid.styles.css';

export const CardGrid = props => (
  <div className='card-grid'>
    {props.items.map(item => (
      <Card dolar={props.dolar} dolarValue={props.dolarValue} key={item.id} item={item} route={props.route}/>
    ))}
  </div>
);
