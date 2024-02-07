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
                            {/* <li> <Link to="/">Home</Link></li> */}
                            {/* <li> <Link to="/resume">Resume</Link></li> */}
                            {/* <li> <Link to="/code">Code</Link></li> */}
                            <li> <a href="/CSS583Project">CSS583Project</a></li>
                            {/* <li> <Link to="/personalBlog">Personal Blog</Link></li> */}
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