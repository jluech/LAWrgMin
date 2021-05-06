import React from "react";
import Button from "react-bootstrap/Button";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

import {FileUpload} from "./file-upload";
import {Premises} from "./premises";
import {Claims} from "./claims";
import {ExportToExcel} from "./export-to-excel";
import {isEmptyObject} from "devextreme/core/utils/type";


const api_host = "http://localhost:5000"

// for file upload tutorial, see https://www.nicesnippets.com/blog/react-js-file-upload-example-with-axios

export class Lawrgminer extends React.Component {
    constructor() {
        super();
        this.state = {
            // copy-pasted text to analyze
            inputText: "",

            // uploaded file of user to analyze
            inputFile: null,

            // JSON from backend as input for premise and claim list
            resultJSON: [],

            claims: [],
            premises: [],
            blocks: [],

            // csv from backend to export
            exportData: [],

            // task/file/instance id from backend
            fileId: null
        };
    }

    adjustInputText(event) {
        this.setState({
            inputText: event.target.value
        });
    }

    adjustInputFile(event) {
        if (event.target.files.length > 0) {
            this.setState({
                inputFile: event.target.files[0]
            });
        }
    }

    tagWithText() {
        const {inputText} = this.state;
        const request_url = `${api_host}/api/tagWithText`
        axios.post(request_url, {"text": inputText})
            .then((response) => {
                const data = response.data;
                this.setState({
                    resultJSON: response.data,
                    fileId: data.id,
                    claims: data.claims,
                    premises: data.premises,
                    blocks: data.blocks,
                });
            })
            .catch((err) => {
                console.log("error during request:", request_url, "\n", err);
                alert(`Something went wrong!\nError during request: ${request_url}`);
            });
    }

    tagWithFile() {
        // for file upload tutorial, see https://www.nicesnippets.com/blog/react-js-file-upload-example-with-axios
        const {inputFile} = this.state;
        if (inputFile) {
            // Create an object of formData
            const formData = new FormData();

            // Update the formData object
            formData.append("file", inputFile);

            // Request made to the backend api to send formData object
            const request_url = `${api_host}/api/tagWithFile`
            axios.post(request_url, formData)
                .then((response) => {
                    const data = response.data;
                    this.setState({
                        resultJSON: data,
                        fileId: data.id,
                        claims: data.claims,
                        premises: data.premises,
                        blocks: data.blocks
                    });
                })
                .catch((err) => {
                    console.log("error during request:", request_url, "\n", err);
                    alert(`Something went wrong!\nError during request: ${request_url}`);
                });
        }
    }

    showTaggedFulltext() {
        const {blocks} = this.state;
        if (blocks.length > 0) {
            return blocks.map((block) => {
                const label = block.label.toLowerCase();
                const classes = `block-text ${label === "claim" ? "block-claim" : (label === "premise" ? "block-premise" : "")}`;
                return (
                    <span className={classes} id={`${label}-${block.idx}`} key={`clause-${block.idx}`}>{block.text}</span>
                );
            })
        } else {
            return null;
        }
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
                                  onChange={this.adjustInputText.bind(this)}
                        />
                        <Button variant="outline-light"
                                onClick={this.tagWithText.bind(this)}
                        >Start Tagging</Button>
                    </div>
                    <FileUpload className="section section-file-upload"
                                tagWithFile={this.tagWithFile.bind(this)}
                                adjustInputFile={this.adjustInputFile.bind(this)}
                                inputFile={this.state.inputFile}
                    />
                </div>

                <br />
                {/*TODO: refactor to remove br tags and properly style hr*/}
                <hr className="solid" style={{position: "relative", top: "1em"}} />
                <br />

                {!isEmptyObject(this.state.blocks) &&
                    <>
                        <h4 className="section-title">2. Results</h4>
                        <div className={"miner-results"}>
                            <div className={"miner-results-list"}>
                                <div className={"miner-results-claims"}>
                                    <h5>Claims</h5>
                                    <Claims claims={this.state.claims}/>
                                </div>
                                <div className={"miner-results-premises"}>
                                    <h5>Premises</h5>
                                    <Premises
                                        premises={this.state.premises}/>
                                </div>
                            </div>
                            <div className={"miner-results-text"}>{this.showTaggedFulltext()}</div>
                            <ExportToExcel
                                fileId={this.state.fileId}
                                api_host = {api_host}
                            />
                        </div>
                        <br/>
                    </>
                }
            </div>
        );
    }
}
