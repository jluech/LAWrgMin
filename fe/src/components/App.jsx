import footer from '../images/footerimage.jpg';
import uzh from '../images/uzh.svg';
import './App.css';
import { report } from './data.js';
import Header from "./header";
import Lawrgminer from './lawrgminer';
import Button from 'react-bootstrap/Button';
import React from 'react';
import Footer from "./footer";
import ReportSection from "./reportSection";

class App extends React.Component {

    render() {
        return <div className="App">
            <Header />
            <body>
                <ReportSection />
                <Lawrgminer />
            </body>

            <Footer />
        </div>
    }
}

export default App;
