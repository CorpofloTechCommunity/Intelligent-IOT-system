import React, { Component } from 'react'
import { Navbar, NavbarBrand, NavItem, Nav,Button, Collapse, NavbarToggler, Modal, ModalHeader, ModalBody, Form, FormGroup, Input, Label} from 'reactstrap'
import { NavLink } from 'react-router-dom';


class Header extends Component {
    constructor(props) {
        super(props);
        this.toggleNav = this.toggleNav.bind(this);
        this.toggleModal = this.toggleModal.bind(this);
        this.handleLogin = this.handleLogin.bind(this);
        this.state={
            isNavOpen:false,
            isModalOpen:true
        }
    }

toggleNav() {
    this.setState(
        { isNavOpen: !this.state.isNavOpen }
    );
}

toggleModal() {
    this.setState(
        { isModalOpen: !this.state.isModalOpen }
    );
}

handleLogin(event){
    this.toggleModal();
    alert("Username: "+ this.username.value +" Password: "+this.password.value+" Remember: "+this.remember.checked);
    event.preventDefault();
}

    render() {
        return (
            <div>
                 <Modal isOpen={this.state.isModalOpen} toggle={this.toggleModal}>
                    <ModalHeader toggle={this.toggleModal} className="bg-light text-center"><strong>Login</strong></ModalHeader>
                    <ModalBody>                        
                            <Form onSubmit={this.handleLogin}>
                                <FormGroup>
                                    <Label htmlFor="username">Username</Label>
                                    <Input type="text" id="username" name="username" innerRef={(input) => this.username = input}></Input>
                                </FormGroup>
                                <FormGroup>
                                    <Label htmlFor="password">password</Label>
                                    <Input type="text" id="password" name="password" innerRef={(input) => this.password = input}></Input>
                                </FormGroup>
                                <FormGroup check>
                                    <Label check>
                                        <Input type="checkbox" name="remember" innerRef={(input) => this.remember = input}></Input>
                                        Remember me
                                    </Label>
                                </FormGroup>
                                <Button type="submit" value="submit" color="primary">Login</Button>
                            </Form>
                    </ModalBody>
                </Modal>
                <Navbar light color="faded" expand="md" className="navbar">
                    <div className="container">
                    <NavbarToggler className="mr-0" onClick={this.toggleNav}/>
                        <NavbarBrand className="ml-0">
                            <NavLink to="/home">
                                <h3 className="text-warning">CORPOFLO</h3>
                            </NavLink>
                        </NavbarBrand>
                        <Collapse  isOpen={this.state.isNavOpen} navbar toggle={this.toggleNav}>
                            <Nav navbar className="ml-auto">
                                <NavItem>
                                    <NavLink to="/home" className="nav-link">
                                        <span className="fa fa-home fa-lg"></span> Home
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink to="/about" className="nav-link">
                                            <span className="fa fa-info fa-lg"></span> About
                                    </NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink to="/contact-Us" className="nav-link">
                                            <span className="fa fa-address-card fa-lg"></span> Contact us
                                    </NavLink>
                                </NavItem>
                            </Nav>
                        </Collapse>
                        <NavItem  to="/contact-Us" className="nav-link"  onClick={this.toggleModal}>
                                        <span className="fa fa-sign-in nav-link login"> Login</span>
                        </NavItem>
                    </div> 
                </Navbar>
            </div>
        )
    }
}

export default Header;
