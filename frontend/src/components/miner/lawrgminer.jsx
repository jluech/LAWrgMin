import React from "react";
import {Button, Spinner} from "react-bootstrap";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import {isEmptyObject} from "devextreme/core/utils/type";
import {alert} from "devextreme/ui/dialog";

import {FileUpload} from "./file-upload";
import {Premises} from "./premises";
import {Claims} from "./claims";
import {ExportToExcel} from "./export-to-excel";

const api_host = "http://localhost:5000";

// for file upload tutorial, see https://www.nicesnippets.com/blog/react-js-file-upload-example-with-axios

export class Lawrgminer extends React.Component {
    constructor() {
        super();
        this.state = {
            // copy-pasted text or uploaded file to analyze
            inputText: "",
            inputFile: null,
            isAwaitingText: false,
            isAwaitingFile: false,

            // results from backend as input for premise/claim list and tagged fulltext
            claims: [],
            premises: [],
            blocks: [],

            // task/file/instance id from backend
            fileId: null,
        };

        // this.inputTextarea ref set in render()
        this.inputFileUpload = React.createRef();
    }

    adjustInputText(event) {
        this.setState({
            inputText: event.target.value,
        });
    }

    adjustInputFile(event) {
        if (event.target.files.length > 0) {
            this.setState({
                inputFile: event.target.files[0],
            });
        }
    }

    tagWithText() {
        const {inputText} = this.state;
        if (!inputText || inputText.length === 0) {
            alert("Please paste some text for tagging first.", "Input Error");
            return;
        }

        this.setState({
            inputFile: null,
            isAwaitingText: true,
            claims: [],
            premises: [],
            blocks: [],
        });
        this.inputFileUpload.current.value = null; // indirect ref in child component so via current

        const request_url = `${api_host}/api/tagWithText`;
        axios
            .post(request_url, {text: inputText})
            .then((response) => {
                const data = response.data;
                this.setState({
                    fileId: data.id,
                    claims: data.claims,
                    premises: data.premises,
                    blocks: data.blocks,
                });
            })
            .catch((err) => {
                console.log("error during request:", request_url, "\n", err);
                alert(`Something went wrong!\nError during request: ${request_url}`, "Tagging Error");
            })
            .finally(() =>
                this.setState({
                    isAwaitingText: false,
                })
            );
    }

    tagWithFile() {
        // for file upload tutorial, see https://www.nicesnippets.com/blog/react-js-file-upload-example-with-axios
        const {inputFile} = this.state;

        if (inputFile) {
            this.setState({
                inputText: "",
                isAwaitingFile: true,
                claims: [],
                premises: [],
                blocks: [],
            });
            this.inputTextarea.value = ""; // direct ref in component so direct access

            // Create an object of formData
            const formData = new FormData();

            // Update the formData object
            formData.append("file", inputFile);

            // Request made to the backend api to send formData object
            const request_url = `${api_host}/api/tagWithFile`;
            axios
                .post(request_url, formData)
                .then((response) => {
                    const data = response.data;
                    this.setState({
                        fileId: data.id,
                        claims: data.claims,
                        premises: data.premises,
                        blocks: data.blocks,
                    });
                })
                .catch((err) => {
                    console.log("error during request:", request_url, "\n", err);
                    alert(`Something went wrong!\nError during request: ${request_url}`, "Tagging Error");
                })
                .finally(() =>
                    this.setState({
                        isAwaitingFile: false,
                    })
                );
        }
    }

    showTaggedFulltext() {
        const {blocks} = this.state;
        if (blocks.length > 0) {
            return blocks.map((block) => {
                const label = block.label.toLowerCase();
                const classes = `block-text ${
                    label === "claim" ? "block-claim" : label === "premise" ? "block-premise" : ""
                }`;
                return (
                    <span className={classes} id={`${label}-${block.idx}`} key={`clause-${block.idx}`}>
                        {block.text}
                    </span>
                );
            });
        } else {
            return null;
        }
    }

    render() {
        return (
            <div className={"lawrgminer"}>
                <h2 className="section-title">I am the LAWrgMiner</h2>
                <h3 className="section-title">Argumentation Mining in Law</h3>

                <h4 className="section-title">1. Input: Paste some text...</h4>
                <div className={"miner-input"}>
                    <div className={"input-textarea"}>
                        <textarea
                            name="miner-input-textarea"
                            id="miner-input-textarea"
                            cols="30"
                            rows="10"
                            onChange={this.adjustInputText.bind(this)}
                            ref={(el) => (this.inputTextarea = el)}
                        />
                        <Button variant="outline-light" onClick={this.tagWithText.bind(this)}>
                            {this.state.isAwaitingText ? (
                                <span className={"input-btn-text"}>
                                    <Spinner animation={"border"} size={"sm"} role={"status"} as={"span"} />
                                    <span>...Tagging</span>
                                </span>
                            ) : (
                                <span className={"input-btn-text"}>Start Tagging</span>
                            )}
                        </Button>
                    </div>
                    <FileUpload
                        className="section section-file-upload"
                        tagWithFile={this.tagWithFile.bind(this)}
                        adjustInputFile={this.adjustInputFile.bind(this)}
                        inputFile={this.state.inputFile}
                        isAwaitingFile={this.state.isAwaitingFile}
                        setRef={this.inputFileUpload}
                    />
                </div>

                <hr className="solid results-separator" />

                {!isEmptyObject(this.state.blocks) && (
                    <>
                        <h4 className="section-title">2. Results</h4>
                        <div className={"miner-results"}>
                            <div className={"miner-results-list"}>
                                <div className={"miner-results-claims"}>
                                    <h5>Claims</h5>
                                    <Claims claims={this.state.claims} />
                                </div>
                                <div className={"miner-results-premises"}>
                                    <h5>Premises</h5>
                                    <Premises premises={this.state.premises} />
                                </div>
                            </div>
                            <div className={"miner-results-text"}>{this.showTaggedFulltext()}</div>
                            <ExportToExcel fileId={this.state.fileId} api_host={api_host} />
                        </div>
                        <br />
                    </>
                )}
            </div>
        );
    }
}
