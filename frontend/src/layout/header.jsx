import React from "react";
import {Link} from "react-scroll";
import "bootstrap/dist/css/bootstrap.min.css";

import uzh from "../images/uzh.svg";

export class Header extends React.Component {


    render() {
        return (
            <header className="app-header text-left">
                <div>
                    <a className={"app-header-uzh-logo"} href="https://www.oec.uzh.ch">
                        <img src={uzh} alt={""} />
                    </a>
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
