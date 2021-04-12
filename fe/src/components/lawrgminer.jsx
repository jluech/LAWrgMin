import React from 'react';
import {report} from "./data";
import uzh from "../images/uzh.svg";

class Lawrgminer extends React.Component {
    render() {
        return <div id='lawrgminer' style={{backgroundColor:'lightgray'}}>
            <h2 id='introduction' className="section">LAWrgMiner</h2>
            <h3 className="section">Argumentation Mining in Law</h3>
            <div >
                <h4 className='section'>1. Text Input</h4>
                <hr className="solid" style={{position:'relative', top:'1em', left:'3em'}}/>

            </div>
        </div>;
    }
}

export default Lawrgminer;