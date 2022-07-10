import './Home.css';
import React from "react";
import useAuth from '../hooks/useAuth';
import 'bulma/css/bulma.min.css';
import { Section, Button } from 'react-bulma-components';

const APP_NAME = 'UCFriends';

function Home() {
    const { auth } = useAuth();

    return(
        <Section className="margins">
            <p>Bienvenid@ a <b><i>{APP_NAME}</i></b>.</p>
            <br />
            <p>
                Después de años de encierro prolongado para buena parte de la población, la creación de nuevas amistades y relaciones se ha dificultado muchísimo. Muchas personas han perdido habilidades de interacción y muchos grupos de intereses comunes se disolvieron dejando a las personas solas o solamente con las relaciones más fuertes, perdiendo sus relaciones más periféricas.
                <br /><br />
                En vista de este gran problema, hemos decidido crear <b><i>{APP_NAME}</i></b>, la plataforma que te permitirá conocer gente con intereses similares a ti en base a los lugares que visitas.
                <br /><br />
                Una vez que te registres podrás consultar por los lugares donde estuvo otra persona registrada en la plataforma para que puedas comparar y ver puntos geográficos donde coinciden.
            </p>
            <br />
            <section>
                {
                    auth ? (
                        auth.user ? (
                            <Button.Group>
                                <Button fullwidth rounded color="primary" renderAs="a" href="/users" >Ver usuarios</Button>
                            </Button.Group>
                        ) : (
                            <Button.Group>
                                <Button fullwidth rounded color="primary" renderAs="a" href="/session/register" >Comienza Aquí</Button>
                            </Button.Group>
                        )
                    ) : (
                        <Button.Group>
                                <Button fullwidth rounded color="primary" renderAs="a" href="/session/register" >Comienza Aquí</Button>
                        </Button.Group>
                    )
                }
            </section>
        </Section>
    );
}

export default Home;
