import "./App.css";
import {Header} from "./header";
import {Lawrgminer} from "./lawrgminer";
import React from "react";
import {Footer} from "./footer";
import {ReportSection} from "./reportSection";

export class App extends React.Component {
    render() {
        return (
            <div className="App">
                <Header />
                <body>
                    <ReportSection />
                    <Lawrgminer />
                </body>

                <Footer />
            </div>
        );
    }
}
