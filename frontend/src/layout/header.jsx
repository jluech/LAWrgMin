import React from "react";
import {Link} from "react-scroll";
import "bootstrap/dist/css/bootstrap.min.css";

import logo from "../images/logo.png";

export class Header extends React.Component {


    render() {
        return (
            <header className="app-header text-left">
                <div>
                    <img style={{maxWidth: "400px"}} src={logo} alt={""} />
                    <div className={"app-header-text"}>
                        <h1>Argumentation Mining in Law</h1>
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
