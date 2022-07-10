import React from 'react';
import './navbar.styles.css';

export const AuthNavBar = props => (
    <div className='navbar'>
        <div className='disclaimer'>DISFRUTA 15% DE DESCUENTO AL SUSCRIBIRTE A NUESTRO NEWSLETTER </div>
        <div className='content'>
            <h1 className='column logo'>LOGO</h1>
            <div className='utils-container column'>
                {props.route === 'Login' && <a href='/signup'>Registrarme</a>}
            </div>
        </div>
    </div>
);

