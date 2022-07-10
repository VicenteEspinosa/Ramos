import { useRef, useState } from 'react';
import useAuth from '../../hooks/useAuth';
import { Link } from 'react-router-dom';
import { connectWebSocket } from './Messager';

// Bulma and Icons
import { Button, Form, Icon } from "react-bulma-components";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faLock, faCircleCheck } from '@fortawesome/free-solid-svg-icons'
import { LoginGoogle } from "./LoginGoogle";

const Login = ({ setClient }) => {
    const { setAuth } = useAuth();

    const userRef = useRef();
    const errRef = useRef();

    const [user, setUser] = useState('');
    const [pwd, setPwd] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const username = user;
            const password = pwd;
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            };
            const response = await fetch(`${process.env.REACT_APP_URL_BACK}/session/login`, requestOptions);
            if (!response.ok) {
                const error = await response.text();
                throw new Error(error);
            }
            setSuccess(true);
            const accessToken = await response.text();
            const pars = JSON.parse(accessToken);
            const token = pars.token;
            // for debugging purposes

            setAuth({ user, pwd, token });
            setUser('');
            setPwd('');
            
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
                        Sesión iniciada con éxito
                        <Icon size="large">
                            <FontAwesomeIcon icon={faCircleCheck} />
                        </Icon>
                    </h1>
                </section>
            ) : (
                <section className="margins">
                    <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    <h1 className="title">Sign In</h1>
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
                        <Form.Label htmlFor="password">Password</Form.Label>
                        <Form.Control>
                          <Form.Input
                              type="password"
                              id="password"
                              onChange={(e) => setPwd(e.target.value)}
                              value={pwd}
                              required
                              placeholder="Password"/>
                          <Icon align="left">
                              <FontAwesomeIcon icon={faLock} />
                          </Icon>
                        </Form.Control>
                    </Form.Field>
                    <Button.Group>
                        <Button fullwidth rounded color="primary" onClick={handleSubmit} >Login</Button>
                    </Button.Group>
                    <LoginGoogle setSuccess = { setSuccess } />
                    <p>
                        Need an Account?<br />
                        <span className="line">
                            <Link to="/session/register">Sign Up</Link>
                        </span>
                    </p>
                </section>
            )}
        </>
    )
}

export default Login