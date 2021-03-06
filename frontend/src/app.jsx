import React from "react";

import "./scss/app.scss";
import {Header} from "./layout/header";
import {Lawrgminer} from "./components/miner/lawrgminer";
import {Footer} from "./layout/footer";
import {ReportSection} from "./components/report/report-section";

export class App extends React.Component {
    render() {
        return (
            <>
                <Header />
                <div className={"content-wrapper"}>
                    <ReportSection />
                    <Lawrgminer />
                </div>
                <Footer />
            </>
        );
    }
}
