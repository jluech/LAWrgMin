import React from "react";
import {FileUpload} from "./fileupload";
import FileDocumentMultipleOutlineIcon from 'mdi-react/FileDocumentMultipleOutlineIcon';
import {DragAndDrop} from "./draganddrop";

export class Lawrgminer extends React.Component {
    constructor() {
        super();
        this.state = {
            files: ["testfile.pdf"],
        };
    }

    render() {
        return (
            <div id="lawrgminer" style={{backgroundColor: "lightgray"}}>
                <h2 id="introduction" className="section-title">
                    I am the LAWrgMiner
                </h2>
                <h3 className="section-title">Argumentation Mining in Law</h3>
                <div>
                    <h4 className="section-title">1. Text Input</h4>
                    <span style={{display: "flex", justifyContent:"center", alignItems:"center"}}>
                        <DragAndDrop>
                            <div className="section" style={{display: "flex", height: 300, width: 300, border: "dashed grey 4px", justifyContent:"center", alignItems:"center"}}>
                                <h3>Drag a PDF here!</h3>
                                <FileDocumentMultipleOutlineIcon/>
                            </div>
                        </DragAndDrop>
                        <FileUpload className="section"/>
                    </span>
                </div>
                <br/>
                <hr className="solid" style={{position: "relative", top: "1em", left: "3em"}} />
                <br/>
                <div>
                    <h4 className="section-title">2. Results</h4>
                    <hr className="solid" style={{position: "relative", top: "1em", left: "3em"}} />

                    <span style={{display: "flex", justifyContent:"center", alignItems:"center"}}>

                    </span>
                </div>
            </div>
        );
    }
}
