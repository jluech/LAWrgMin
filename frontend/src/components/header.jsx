import React from "react";
import header_img from "../images/header_img.jpg";
import uzh from "../images/uzh.svg";
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import {NavLink} from "react-bootstrap";
import {Link} from 'react-scroll';




export class Header extends React.Component {

    render() {
        return <div className="App">
            <header className="App-header" style= { {
                backgroundImage: `url(${header_img})`
            }}>
                <div>
                    <img src={uzh} alt={""}/>
                    <ul style={{
                        listStyle: 'none',
                        display: 'inline-flex',
                        position:'fixed',
                        right:'10px'
                    }}>
                        <NavLink />
                        <li style={{padding: '2em'}}>
                            <Link activeClass="active" to="introduction" spy={true} smooth={true}>Project</Link>
                        </li>
                        <li style={{padding: '2em'}}>
                            <Link activeClass="active" to="lawrgminer" spy={true} smooth={true}>LAWrgMiner</Link>
                        </li>
                    </ul>
                    <h1 style={{paddingTop: '8em', paddingLeft:'2em'}}>LAWrgMiner Project</h1>
                    <hr className="solid" style={{position:'relative', top:'1em', left:'3em'}}/>
                    <h6 style={{position:'relative', top:'2em', left:'5em'}}>Artificial Intelligence: Technology and Law</h6>
                    <Button style={{position:'relative', top:'3em', left:'5em'}} variant="outline-light" >Use LAWrgMiner</Button>
                    <div>
                        <br/>
                        <br/>
                        <br/>
                        <br/>
                    </div>
                </div>
            </header>
        </div>
    }
}

