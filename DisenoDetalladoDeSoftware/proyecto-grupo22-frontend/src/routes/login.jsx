import React, { Component } from 'react';
import { AuthNavBar } from '../components/navbar/authNav';
import './admin.css';

class Login extends Component {
    constructor() {
        super();

        this.state = {
          email: '',
          password: '',
          feedbackLogin: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/users/sign_in`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: this.state.email, password: this.state.password })
        }).then(response => response.json())
          .then(data => {
            if (data.user) {
                this.setState({ feedbackLogin: '', user: data.user });
                this.props.setUser(data.user);
                this.props.onRouteChange('home');

            } else {
                this.setState({ feedbackLogin: 'Ocurrió un error. Inténtalo nuevamente' });
            }
          })
        event.preventDefault();
    }

    handleChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
          [name]: value
        });
    }

    render() {
        return (
            <div className='Login'>
                <AuthNavBar route='Login' />
                <div className='login-container'>
                    <form  className='login-container' onSubmit={this.handleSubmit}>
                        <label>
                            Email:
                            <input type="email" name="email" onChange={this.handleChange} />
                        </label>
                        <label>
                            Contraseña:
                            <input type="password" name="password" onChange={this.handleChange} />
                        </label>
                        <input type="submit" value="Submit" />
                    </form>
                    <p>{this.state.feedbackLogin}</p>
                </div>
            </div>
        );
    }
}

export default Login;
