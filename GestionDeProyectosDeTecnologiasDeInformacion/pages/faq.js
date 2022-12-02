import Layout from "../components/layout";
import style from "../styles/faq.module.css";

export default function FAQ() {
  return (
    <Layout>
      <div className={style.faq}>
        <h2 align='center'>Preguntas frecuentes</h2>

        <div>
          <h3>¿Dónde puedo buscar un evento?</h3>
          <p>
            En la página de Buscar por fecha, puedes buscar un evento por una fecha en específico.
          </p>
          <h3>¿Puedo comprar las entradas acá?</h3>
          <p>
            No, esta página solo muestra las distintas opciones de eventos que hay en la ciudad.
          </p>
        </div>
      </div>
    </Layout>
  );
}
