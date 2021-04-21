import React from "react";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import FileDocumentMultipleOutlineIcon from "mdi-react/FileDocumentMultipleOutlineIcon";

import "../../scss/lawrgminer.scss";
import {FileUpload} from "./file-upload";
import {DragAndDrop} from "./drag-and-drop";
import {Arguments} from "./arguments";
import {Claims} from "./claims";

export class Lawrgminer extends React.Component {
    constructor() {
        super();
        this.state = {
            files: ["testfile.pdf"],
        };
    }

    render() {
        return (
            <div className={"lawrgminer"}>
                <h2 className="section-title">I am the LAWrgMiner</h2>
                <h3 className="section-title">Argumentation Mining in Law</h3>
                <h4 className="section-title">1. Text Input</h4>
                <div className={"miner-input"}>
                    <div className={"input-textarea"}>
                        <textarea name="miner-input-textarea" id="miner-input-textarea"
                                  cols="30" rows="10"
                        />
                        <button>Start Tagging</button>
                    </div>
                    <div className={"input-drag-drop"}>
                        <DragAndDrop>
                            <div className="section section-drag-drop">
                                <h3>Drag a PDF here!</h3>
                                <FileDocumentMultipleOutlineIcon />
                            </div>
                        </DragAndDrop>
                        <FileUpload className="section section-file-upload" />
                    </div>
                </div>
                <br />
                {/*TODO: refactor to remove br tags and properly style hr*/}
                <hr className="solid" style={{position: "relative", top: "1em"}} />
                <br />
                <div className={"miner-results"}>
                    <h4 className="section-title">2. Results</h4>
                    <div className={"miner-results-list"}>
                        <div className={"miner-results-claims"}>
                            <h5>Claims</h5>
                            <Claims />
                        </div>
                        <div className={"miner-results-arguments"}>
                            <h5>Arguments</h5>
                            <Arguments />
                        </div>
                    </div>
                    <Button className={"miner-results-export-btn"} variant="outline-light">
                        Export Data
                    </Button>
                </div>
                <br />
            </div>
        );
    }
}
