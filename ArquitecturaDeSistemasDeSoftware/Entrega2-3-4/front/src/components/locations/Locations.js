import { useState } from "react";
import useAuth from "../../hooks/useAuth";

// Bulma and Icons
import { Button, Form, Icon } from "react-bulma-components";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowsLeftRight, faArrowsUpDown, faCircleCheck, faGlobe } from '@fortawesome/free-solid-svg-icons'

const Locations = () => {
    const { auth } = useAuth();

    const [locationName, setLocationName] = useState('');
    const [latitude, setLatitude] = useState(0);
    const [longitude, setLongitude] = useState(0);

    const tags = ["universidad", "deporte", "entretenimiento", "hogar", "trabajo", "supermercado", "tienda de ropa", "bar", "restaurante", "parque"];
    const [success, setSuccess] = useState(false);

    const [checkedState, setCheckedState] = useState(
        new Array(10).fill(false)
    );

    const handleOnChange = (position) => {
        const updatedCheckedState = checkedState.map((item, index) =>
          index === position ? !item : item
        );
    
        setCheckedState(updatedCheckedState);
    };


    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = auth.token;
            const name = locationName;
            const tags_tf = checkedState;
            const location = { 'type': 'Point', 'coordinates': [latitude, longitude] };

            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'token': token },
                body: JSON.stringify({ name, location, tags_tf }),
            };
            const response = await fetch(`${process.env.REACT_APP_URL_BACK}/locations`, requestOptions);
            if (response.ok) {
                setSuccess(true);
            }
            //clear state and controlled inputs
            setLocationName('');
            setLatitude(0);
            setLongitude(0);
            const error = await response.text();
            throw new Error(error);
        } catch (error) {
            console.log(error)
        }
    }
    return (
        <>
            {success ? (
                <section className="margins">
                    <h1 className="title">
                        Ubicación creada con éxito
                        <Icon size="large">
                            <FontAwesomeIcon icon={faCircleCheck} />
                        </Icon>
                    </h1>
                </section>
            ) : (
                <section className="margins">
                    <h1 className="title">Locations</h1>
                    <Form.Field>
                        <Form.Label htmlFor="name">Location name</Form.Label>
                        <Form.Control>
                            <Form.Input
                                type="text"
                                id="name"
                                autoComplete="off"
                                onChange={(e) => setLocationName(e.target.value)}
                                value={locationName}
                                required
                                placeholder="Location name"
                            />
                            <Icon align="left">
                                <FontAwesomeIcon icon={faGlobe} />
                            </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Form.Field>
                        <Form.Label htmlFor="latitude">Latitude</Form.Label>
                        <Form.Control>
                          <Form.Input
                              type="number"
                              id="latitude"
                              step="0.000001"
                              onChange={(e) => setLatitude(e.target.value)}
                              value={latitude}
                              required
                          />
                          <Icon align="left">
                              <FontAwesomeIcon icon={faArrowsLeftRight} />
                          </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Form.Field>
                        <Form.Label htmlFor="longitude">Longitude</Form.Label>
                        <Form.Control>
                          <Form.Input
                              type="number"
                              id="longitude"
                              step="0.000001"
                              onChange={(e) => setLongitude(e.target.value)}
                              value={longitude}
                              required
                          />
                          <Icon align="left">
                              <FontAwesomeIcon icon={faArrowsUpDown} />
                          </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Form.Field>
                    <Form.Label htmlFor="tags">Etiquetas</Form.Label>
                    {tags.map((item, index) => {
                        return (
                                <Form.Control>
                                  <Form.Checkbox
                                      className="p-2"
                                      value={checkedState[index]}
                                      onChange={() => handleOnChange(index)}
                                      required
                                  />
                                   {item}
                                </Form.Control>
                        );
                    })}	
                    </Form.Field>
                    <Button.Group>
                        <Button fullwidth rounded color="primary" onClick={handleSubmit} >Agregar ubicación</Button>
                    </Button.Group>
                </section>
            )}
        </>
    )
}

export default Locations