import React from "react";
import {Link} from "react-scroll";
import "bootstrap/dist/css/bootstrap.min.css";

import logo from "../images/logo.png";

export class Header extends React.Component {

    render() {
        return (
            <header className="app-header text-left">
                <div>
                    <img className={"app-header-logo"} src={logo} alt={""} />
                    <div className={"app-header-text"}>
                        <h1>Argumentation Mining in Law</h1>
                        <hr className="solid" />
                        <h6>Artificial Intelligence: Technology and Law</h6>
                        <br />
                        <Link
                            className={"app-header-link-lawrgminer"}
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
