import axios from "axios";
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { addDotsToNumber } from "../../utils";
import styles from "./product.module.css";

export default function Product() {
  const [loading, setLoading] = useState(true);
  const [product, setProduct] = useState({});
  const { id, type } = useParams();
  const getData = async () => {
    try {
      const response = await axios.get(`/${type}/${id}`);
      setProduct(response.data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  const redirectProducto = (e, type) => {
    e.preventDefault();
    window.location.replace(`/producto/${e.target.id}/${type}`);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div>
      <div className={styles.columns}>
        <div className={styles.column1}>
          <p className={styles.name}>{product.name}</p>
          {product.price ? (
            <p className={styles.price}>${addDotsToNumber(product.price)}</p>
          ) : null}
          {product.description ? (
            <p className={styles.description}>{product.description}</p>
          ) : null}
          <p className={styles.size}>Tamaño: {product.size}</p>
          <p className={styles.expiration}>Expiración: {product.expiration}</p>
        </div>
        {product.img_url ? (
          <div className={styles.column2}>
            <img className={styles.image} src={product.img_url} alt="product" />
          </div>
        ) : null}
      </div>
      {product.ingredients ? (
        <div className={styles.list}>
          <div className={styles.listHeader}>Ingredientes necesarios: </div>
          <ol>
            {product.ingredients.map((ingredient) => (
              <li
                key={ingredient.id}
                id={ingredient.id}
                onClick={(e) => redirectProducto(e, "ingredients")}
              >
                {ingredient.name} {ingredient.quantity} unidad{" "}
                {ingredient.quantity > 1 ? "es" : ""}
              </li>
            ))}
          </ol>
        </div>
      ) : null}
      {product.courses ? (
        <div className={styles.list}>
          <div className={styles.listHeader}>Platos necesarios:</div>
          <ol>
            {product.courses.map((course) => (
              <li
                key={course.id}
                id={course.id}
                onClick={(e) => redirectProducto(e, "courses")}
              >
                {course.name}
              </li>
            ))}
          </ol>
        </div>
      ) : null}
    </div>
  );
}
