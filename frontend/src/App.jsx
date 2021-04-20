import React from "react";

import "./App.css";
import {Header} from "./layout/header";
import {Lawrgminer} from "./components/miner/lawrgminer";
import {Footer} from "./layout/footer";
import {ReportSection} from "./components/report/reportSection";

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
