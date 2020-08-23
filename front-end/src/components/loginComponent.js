import React, { Component } from 'react';
import {Button, Navbar} from 'reactstrap';
import Header from './HeaderComponent';
import Footer from './FooterComponent';
import Home from './HomeComponent';


class Login extends Component {

    constructor(props) {
        super(props)
        this.state = {
        }
    }

    render() {
        return (
            <div col={12}>
                <Header/>
                <Home/>
                <Footer/>
            </div>
        )
    }
}

export default Login;
