import { useRef, useState } from "react";
import { Link } from "react-router-dom";

// Bulma and Icons
import { Button, Form, Icon } from "react-bulma-components";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faAt, faLock, faCircleCheck } from '@fortawesome/free-solid-svg-icons'

const Register = () => {
    const userRef = useRef();
    const errRef = useRef();

    const [user, setUser] = useState('');

    const [email, setEmail] = useState('');

    const [pwd, setPwd] = useState('');

    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        // if button enabled with JS hack
        try {
            const username = user;
            const password = pwd;
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, email, password }),
            };
            const response = await fetch(`${process.env.REACT_APP_URL_BACK}/session/register`, requestOptions);
            // TODO: remove console.logs before deployment
            if (response.ok) {
                setSuccess(true);
            }
            //clear state and controlled inputs
            setUser('');
            setEmail('');
            setPwd('');
            const error = await response.text();
            throw new Error(error);
        } catch (error) {
            console.log(error)
            setErrMsg(error.message);
        }
    }
    return (
        <>
            {success ? (
                <section className="margins">
                    <h1 className="title">
                        Usuario creado. Ahora puedes iniciar sesión
                        <Icon size="large">
                            <FontAwesomeIcon icon={faCircleCheck} />
                        </Icon>
                    </h1>
                </section>
            ) : (
                <section className="margins">
                    <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    <h1 className="title">Register</h1>
                    <Form.Field>
                        <Form.Label htmlFor="username">Username</Form.Label>
                        <Form.Control>
                            <Form.Input
                                type="text"
                                id="username"
                                href={userRef}
                                autoComplete="off"
                                onChange={(e) => setUser(e.target.value)}
                                value={user}
                                required
                                placeholder="Username"
                            />
                            <Icon align="left">
                                <FontAwesomeIcon icon={faUser} />
                            </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Form.Field>
                        <Form.Label htmlFor="email">Email</Form.Label>
                        <Form.Control>
                          <Form.Input
                              type="text"
                              id="email"
                              autoComplete="off"
                              onChange={(e) => setEmail(e.target.value)}
                              value={email}
                              required
                              placeholder="Email"
                          />
                          <Icon align="left">
                              <FontAwesomeIcon icon={faAt} />
                          </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Form.Field>
                        <Form.Label htmlFor="password">Password</Form.Label>
                        <Form.Control>
                          <Form.Input
                              type="password"
                              id="password"
                              onChange={(e) => setPwd(e.target.value)}
                              value={pwd}
                              required
                              placeholder="Password"
                          />
                          <Icon align="left">
                              <FontAwesomeIcon icon={faLock} />
                          </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Button.Group>
                        <Button fullwidth rounded color="primary" onClick={handleSubmit} >Register</Button>
                    </Button.Group>
                    <p>
                        Already registered?<br />
                        <span className="line">
                            <Link to="/session/login">Sign In</Link>
                        </span>
                    </p>
                </section>
            )}
        </>
    )
}

export default Register