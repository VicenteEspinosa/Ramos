import Layout from "../../components/layout";
import Product from "../../components/product";
import { getItems } from "../../services/storeService";
import ShoppingCart from "../../components/shoppingCart";
import {useState} from 'react'

import styleProduct from "../../styles/product.module.css";

export default function Index() {
    const [search, setSearch] = useState('');
    const [day, setDay] = useState('');
    const [month, setMonth] = useState('enero');
    const [year, setYear] = useState('');

    const [items, setItems] = useState([]);

    const setEvents = (e) => {
        setSearch('buscar');
        var data = require('../../scrapers/json/puntoticket.json');
        var data2 = require('../../scrapers/json/cinehoyts.json');
        var data3 = data.concat(data2);
        var cosas = [];
        console.log(day);
        for (var i = 0; i < data3.length; i++) {
            if (data3[i].startDate == day + " de " + month + " " + year || data3[i].startDate == "0" + day + " de " + month + " " + year || data3[i].startDate == "TE") {
            cosas.push(data3[i]);
            }
        }
        setItems(cosas);
    };

    if (!search) {
        return (
            <Layout>
                <center>
                    <form>
                        <label>Día: <input type="number" name = "day" value={day} min="1" max="31" onChange={(e) => setDay(e.target.value)}/></label>
                        <label>Mes:</label>
                            <select value={month} onChange={(e) => setMonth(e.target.value)}>
                                <option value="enero">Enero</option>
                                <option value="febrero">Febrero</option>
                                <option value="marzo">Marzo</option>
                                <option value="abril">Abril</option>
                                <option value="mayo">Mayo</option>
                                <option value="junio">Junio</option>
                                <option value="julio">Julio</option>
                                <option value="agosto">Agosto</option>
                                <option value="septiembre">Septiembre</option>
                                <option value="octubre">Octubre</option>
                                <option value="noviembre">Noviembre</option>
                                <option value="diciembre">Diciembre</option>
                            </select>
                        <label>Año: <input type="number" name="year" value={year} min="2022" onChange={(e) => setYear(e.target.value)}/></label>
                        <button type="submit" onClick={setEvents}>Buscar</button>
                    </form>
                </center>
            </Layout>
        );
    }

    else {
        return (
            <Layout>
                <center>
                    <form>
                        <button type="submit" onClick={(e) => setSearch('')}>Buscar otra fecha</button>
                    </form>
                </center>
                <p>Fecha buscada: {day + " de " + month + " " + year}</p>
                <div className={styleProduct.items}>
                    {items &&
                    items.map((item) => (
                        <Product key={item.id} item={item} showAs="item" />
                    ))}
                </div>
            </Layout>
        );
    }
}
/*
export async function getStaticProps( {form} ) {
    var data = require('../../scrapers/json/puntoticket.json');
    var data2 = require('../../scrapers/json/cinehoyts.json');
    var data3 = data.concat(data2);
    var items = [];
    console.log(form)
    for (var i = 0; i < data3.length; i++) {
        if (data3[i].startDate == form.day + " de " + convertMonth(form.month) + " " + form.year) {
        items.push(data3[i]);
        }
    }
    return {
        props: {
        items: items,
        },
    };
}
*/
