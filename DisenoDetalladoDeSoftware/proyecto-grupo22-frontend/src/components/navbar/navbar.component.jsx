import React from 'react';
import './navbar.styles.css';
import { BsHeartFill } from 'react-icons/bs'
import { FaShoppingCart, FaHistory } from 'react-icons/fa'
import { RiCoupon2Line } from 'react-icons/ri';

export const NavBar = props => (
    <div className='navbar'>
        {props.route === 'Admin' ? <div /> : <div className='disclaimer'>DISFRUTA 15% DE DESCUENTO AL SUSCRIBIRTE A NUESTRO NEWSLETTER </div>}
        <div className='content'>
            {props.route === 'Admin' ? <h2 className='column'>Admin</h2> : <div className='column'/>}
            <a className='column logo' href='/'><h1 className='column logo'>LOGO</h1></a>
            <div className='utils-container column'>
                <a className='auth' href='/logout'>Hola {props.username} / Cerrar Sesión</a>
                {props.route !== 'Admin' && <a href='/#'><BsHeartFill /></a> }
                {props.route !== 'Admin' && <a href='/cart'>Carrito <FaShoppingCart /></a>}
                {props.route !== 'Admin' && <a href='/coupons'>Cupones <RiCoupon2Line /></a>}
                {props.route !== 'Admin' && <a href='/purchases'>Mis Compras <FaHistory /></a>}
            </div>
        </div>
    </div>
);

