import footer from '../images/footerimage.jpg';
import './App.css';
import React from 'react';

export class Footer extends React.Component {

    render() {
        return <div className="App">
            <footer className="App-footer" style= { {
                backgroundImage: `url(${footer})`
            }}>
                <div className="header-footer-content-box" style={{position:"relative", left:"10%"}}>
                    <h3>AI Technology and Law</h3>
                    <hr className="solid"/>
                    <h6>Course: AI: Technology and Law (FS21)</h6>
                    <h6>Lecturers: Prof. Abraham Bernstein PhD & Prof. Dr. Florent Thouvenin</h6>
                    <h6>The research project was executed by Tjasa Marincek, Janik Lüchinger, Damaris Schmid, Cédric Zellweger & Adrian Zermin</h6>
                </div>
            </footer>
        </div>
    }
}
