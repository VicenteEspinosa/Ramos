import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route, } from "react-router-dom";
import './index.css';
import App from './App';
import Admin from './routes/admin';
import { ShoppingCart } from './components/shoppingCart/shoppingCart';
import Coupons from './components/Coupons/Coupons';
import Purchases from './components/Purchases/Purchases';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/admin" element={<Admin />} />
      <Route path="/cart" element={<ShoppingCart/>}/>
      <Route path="/coupons" element={<Coupons/>}/>
      <Route path="/purchases" element={<Purchases/>}/>
    </Routes>
  </BrowserRouter>,
);
