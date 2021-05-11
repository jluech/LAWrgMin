import React from "react";

import image1 from "../../images/LAWrgMiner_1.jpg";
import image2 from "../../images/LAWrgMiner_2.jpg";
import imagefront from "../../images/LAWrgMiner_front.jpg";

import {report} from "./data.js";

export class ReportSection extends React.Component {
    render() {
        return (
            <div id="project">
                <div className="chapter light">
                    <h2 className="section-title">{report[0].section}</h2>
                    <div className="textbox">
                        <img className="text-image" src={image1} alt={""} />
                        <p className="text">{report[0].text}</p>
                    </div>
                </div>
                <div className="chapter dark">
                    <h2 className="section-title">{report[1].section}</h2>
                    <div className="textbox">
                        <img className="text-image" src={image2} alt={""} />
                        <p className="text">{report[1].text}</p>
                    </div>
                </div>
                <div className="chapter light">
                    <h2 className="section-title">{report[2].section}</h2>
                    <div className="textbox">
                        <img className="text-image" src={imagefront} alt={""} />
                        <p className="text">{report[2].text}</p>
                    </div>
                </div>
                <div className="chapter dark">
                    <h2 className="section-title">{report[3].section}</h2>
                    <div className="textbox">
                        <img className="text-image" src={image2} alt={""} />
                        <p className="text">{report[3].text}</p>
                    </div>
                </div>
            </div>
        );
    }
}
