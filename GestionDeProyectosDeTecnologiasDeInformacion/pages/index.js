import Link from "next/link";
import Image from "next/image";
import Layout from "../components/layout";
import ShoppingCart from "../components/shoppingCart";
import Product from "../components/product";
import style from "../styles/Home.module.css";
import { getLatestItems } from "../services/storeService";
import styleProduct from "../styles/product.module.css";

export default function Home({ items }) {
  return (
    <div>
      <Layout>
        <div className={style.banner}>
          <div className={style.bannerBackground}>
            <div className={style.bannerInfo}>
              <h2>Búsqueda de eventos en Santiago</h2>
              <p>
                Busca el evento que más te acomode
                dentro de Santiago, para las fechas que 
                tu prefieras!!
              </p>
            </div>
          </div>
        </div>

        <h2>
          <center>Últimos Eventos</center>
        </h2>
        <div className={styleProduct.items}>
          {items &&
            items.map((item) => (
              <Product key={item.id} item={item} showAs="item" />
            ))}
        </div>
      </Layout>
    </div>
  );
}

export async function getStaticProps() {
  var data = require('../scrapers/json/puntoticket.json').slice(0,3);
  return {
    props: {
      items: data,
    },
  };
}
