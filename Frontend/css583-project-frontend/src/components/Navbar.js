import React, { Component } from "react"; 
import { Link } from 'react-router-dom'; 
import { ReactComponent as Logo } from "./logoipsum-274.svg";
import './Navbar.css'; 

class Navbar extends Component{
    state = { clicked: false};
    handleClick = () => {
        this.setState({clicked: !this.state.clicked})
    }
    render () {

        return(
            <>
                <nav>
                    <a href="/">
                    <Logo />
                    </a>

                    <div>
                        <ul id="navbar" className={this.state.clicked ? "#navbar active" : "#navbar"}>
                            <li> <a href="/CSS583Project">CSS583Project</a></li>
                        </ul>
                    </div>

                    <div id="mobile" onClick={this.handleClick}>
                        <i id="bar" className={this.state.clicked? "fas fa-times" : "fas fa-bars"}></i>
                    </div>
                </nav>
            </>
        )
    }
}

export default Navbar; 