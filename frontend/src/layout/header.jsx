import React from "react";
import {Link} from "react-scroll";
import "bootstrap/dist/css/bootstrap.min.css";

import uzh from "../images/uzh.svg";

export class Header extends React.Component {
    render() {
        return (
            <header className="app-header text-left">
                <div>
                    <img src={uzh} alt={""} />
                    <ul
                        style={{
                            listStyle: "none",
                            display: "inline-flex",
                            position: "fixed",
                            right: "10px",
                        }}
                    >
                        <li style={{padding: "2em"}}>
                            <Link activeClass="active" to="introduction" spy={true} smooth={true}>
                                Project
                            </Link>
                        </li>
                        <li style={{padding: "2em"}}>
                            <Link activeClass="active" to="lawrgminer" spy={true} smooth={true}>
                                LAWrgMiner
                            </Link>
                        </li>
                    </ul>

                    <div style={{marginLeft: "30%", marginTop: "10%"}}>
                        <h1>LAWrgMiner Project</h1>
                        <hr className="solid" />
                        <h6>Artificial Intelligence: Technology and Law</h6>
                        <br />
                        <Link
                            style={{
                                border: "1px solid white",
                                borderRadius: "10px",
                                padding: "1em 2em",
                                fontSize: "20px",
                            }}
                            activeClass="active"
                            to="lawrgminer"
                            spy={true}
                            smooth={true}
                        >
                            Use LAWrgMiner
                        </Link>
                    </div>
                    <br />
                    <br />
                    <br />
                    <br />
                </div>
            </header>
        );
    }
}
