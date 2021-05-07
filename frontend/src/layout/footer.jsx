import React from "react";

import footerImg from "../images/footerimage.jpg";
import {report} from "../components/report/data";

export class Footer extends React.Component {
    render() {
        return (
            <footer
                className="app-footer text-left"
                style={{
                    backgroundImage: `url(${footerImg})`,
                }}
            >
                <div className="footer-content-box" style={{position: "relative", left: "10%"}}>
                    <h3>AI Technology and Law</h3>
                    <hr className="solid" />
                    <div>Course: AI: Technology and Law (FS21)</div>
                    <div>Lecturers: Prof. Abraham Bernstein PhD & Prof. Dr. Florent Thouvenin</div>
                    <br/>
                    <div>
                        The research project was executed by Tjasa Marincek, Janik Lüchinger, Damaris Schmid,
                        Cédric Zellweger, & Adrian Zermin
                    </div>
                    <br/>
                    <div className={"footer-references"}>
                        <div className={"footer-reference-title"}>References</div>
                        <div className={"footer-reference-entries"}>
                            {report[4].text.map((entry, index) => <span className={"footer-reference-entry"} key={`footer-ref-${index}`}>{entry}</span>)}
                        </div>
                    </div>
                </div>
            </footer>
        );
    }
}
