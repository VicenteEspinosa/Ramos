import { useEffect, useState } from "react";
import useAuth from '../../hooks/useAuth';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSun, faCloudRain } from '@fortawesome/free-solid-svg-icons'
import { Button, Icon } from "react-bulma-components";
import { useParams } from "react-router-dom";

const OtherProfile = () => {
  const { auth } = useAuth();
  const { id } = useParams();
  const [userData, setUserData] = useState();
  const [locations, setLocations] = useState([]);
  const [api, setApi] = useState([]);

  const createPing = async () => {
    try {
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'token': auth.token },
        body : JSON.stringify({
          'to': id,
          'status': 'pending'
        })
      };
      const response = await fetch(`${process.env.REACT_APP_URL_BACK}/pings`, requestOptions);
      if (!response.ok) {
        const error = await response.text();
        throw new Error(error);
    }
  } catch (error) {
    console.log(error);
  }
  }


  useEffect(() => {
    const getUserData = async () => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/users/${id}`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const rawData = await response.text();
        const data = JSON.parse(rawData);
        setUserData(data);

        data.locations.map(locationID => addLocationByID(locationID));
      } catch (error) {
        console.log(error);
      }
    }

    const addLocationByID = async locationID => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/locations/${locationID}`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const rawData = await response.text();
        const data = JSON.parse(rawData);
        // NOTA: La siguiente linea produce resultados duplicados al utilizar StrictMode.
        // Es porque agrega cosas al arreglo cada vez que se renderiza el componente, entonces el arreglo
        // solo se reinicia cada vez que llega al end point por primera vez.
        setLocations(oldData => [...oldData, data]);
      } catch (error) {
        console.log(error);
      }
      return null;
    }

    const getAPI = async () => {
      try {
        const requestOptions = {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(`${process.env.REACT_APP_URL_BACK}/locations/api/weather`, requestOptions);
        if (!response.ok) {
          const error = await response.text();
          throw new Error(error);
        }

        const data = await response.json();
        setApi(data);
      } catch (error) {
        console.log(error);
      }
      return null;
    }

    getUserData();
    getAPI();

  }, [id]);

  return (
    <>
      {
        userData ? (
          <article className="margins">
            <div class="columns is-vcentered">
              <div class="column is-8">
                <h1 className="title">User Profile</h1>
                <h2 className="subtitle is-5">Username: {userData.username}</h2>
                <h2 className="subtitle is-5">Email: {userData.email}</h2>
              </div>
              <div class="column">
                <Button.Group>
                    <Button class="button is-primary is-pulled-right" rounded color="primary" onClick={createPing}>Hacer Ping</Button>
                </Button.Group>
                <Button.Group>
                  <a href="/#">
                    <Button class="button is-primary is-pulled-right" rounded color="primary">Comparar Mapas</Button>
                  </a>
                </Button.Group>
              </div>
            </div>
            <br />
            <h2 className="subtitle is-4">My locations:</h2>
            {
              <>
                <ul>
                  {
                    locations.map((location, i) =>
                      <li key={i} className="subtitle is-5">
                        "{location?.name}": ({location?.location.coordinates[0]}, {location?.location.coordinates[1]})
                        {api[0] ? (
                          <Icon size="large">
                            <FontAwesomeIcon icon={faSun} />
                          </Icon>
                        ) : (
                          <Icon size="large">
                            <FontAwesomeIcon icon={faCloudRain} />
                          </Icon>
                        )}
                      </li>)
                  }
                </ul>
                <br />

              </>
            }
          </article>
        ) : null
      }
    </>
  );
};

export default OtherProfile;