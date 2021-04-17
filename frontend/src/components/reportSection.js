import React from "react";

import uzh from "../images/uzh.svg";
import "./App.css";
import {report} from "./data.js";

class ReportSection extends React.Component {
    render() {
        return (
            <div>
                <div className="light">
                    <h2 id="introduction" className="section">
                        {report[0].section}
                    </h2>
                    <div className="textbox">
                        <img className="text-image" src={uzh} alt={"uzh_logo"} />
                        <p className="text">{report[0].text}</p>
                    </div>
                </div>
                <div className="dark">
                    <h2 className="section">{report[1].section}</h2>
                    <div className="textbox">
                        <img className="text-image" src={uzh} alt={"uzh_logo"} />
                        <p className="text">{report[1].text}</p>
                    </div>
                </div>
            </div>
        );
    }
}

export default ReportSection;
