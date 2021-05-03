import React from "react";

import footer from "../images/footerimage.jpg";

export class Footer extends React.Component {
    render() {
        return (
            <footer
                className="app-footer text-left"
                style={{
                    backgroundImage: `url(${footer})`,
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
                </div>
            </footer>
        );
    }
}
