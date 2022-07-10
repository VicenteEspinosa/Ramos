import './CustomNavbar.css';
import React from "react";
import useAuth from '../hooks/useAuth';
import { Section, Navbar, Icon } from 'react-bulma-components';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHouse } from '@fortawesome/free-solid-svg-icons'

function CustomNavbar() {
    const { auth, setAuth } = useAuth();

    const logout = async () => {
        setAuth({});
    }

    const toggleBurgerMenu = () => {
      document.querySelector('.navbar-menu').classList.toggle('is-active');
    }

    return(
        <Section>
            <Navbar className="navbar">
                <Navbar.Brand>
                    <Navbar.Item renderAs="a" href="/">
                        <Icon>
                            <FontAwesomeIcon icon={faHouse} />
                        </Icon>
                    </Navbar.Item>
                    <Navbar.Burger onClick={toggleBurgerMenu}>
                    </Navbar.Burger>
                </Navbar.Brand>
                <Navbar.Menu>
                    <Navbar.Container>
                        <Navbar.Item href="/users">Ver Usuarios</Navbar.Item>
                        <Navbar.Item href="/findLocation">Ver Ubicaciones por Usuario</Navbar.Item>
                        {
                            auth ? (
                                auth.user ? (
                                    <>
                                    <Navbar.Item href="/users/profile">Mi Perfil</Navbar.Item>
                                    <Navbar.Item href="/chatList">Mis Chats</Navbar.Item>
                                    </>
                                ) : (
                                    <>
                                        <Navbar.Item href="/session/login">Ingresar</Navbar.Item>
                                        <Navbar.Item href="/session/register">Registrarse</Navbar.Item>
                                    </>
                                )
                            ) : (
                                <>
                                    <Navbar.Item href="/session/login">Ingresar</Navbar.Item>
                                    <Navbar.Item href="/session/register">Registrarse</Navbar.Item>
                                </>
                            )
                            
                        }
                    </Navbar.Container>
                    <Navbar.Container position="end" className="align-right">
                        {
                            auth ? (
                                auth.user ? <Navbar.Item href="/" onClick={logout}>Sign Out</Navbar.Item> : null
                            ) : (
                                <Navbar.Item href="/" onClick={logout}>Sign Out</Navbar.Item>
                            )
                        }
                    </Navbar.Container>
                </Navbar.Menu>
            </Navbar>
        </Section>
    );
}

export default CustomNavbar;
