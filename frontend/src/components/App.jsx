import React from "react";

import "./App.css";
import Header from "./header";
import Lawrgminer from "./lawrgminer";
import Footer from "./footer";
import ReportSection from "./reportSection";

class App extends React.Component {
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

export default App;
