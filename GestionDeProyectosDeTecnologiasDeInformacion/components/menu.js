import Link from "next/link";

import style from "../styles/menu.module.css";
import { useAppContext } from "./stateWrapper";

export default function Menu() {
  const cart = useAppContext();

  function handleClickCart(e) {
    e.preventDefault();
    cart.openCart();
  }
  return (
    <nav className={style.menu}>
      <div>
        <Link href="/">
          <a className={style.link}>Inicio</a>
        </Link>

        <Link href="/eventos">
          <a className={style.link}>Eventos</a>
        </Link>

        <Link href="/faq">
          <a className={style.link}>FAQ</a>
        </Link>

        <Link href="/buscar">
          <a className={style.link}>Buscar en fecha</a>
        </Link>
        
        <h4>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        HOTEL: Descanso Bellavista 
        </h4>

      </div>

      <div></div>
    </nav>
  );
}
