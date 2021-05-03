import React from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

import {FileUpload} from "./file-upload";
import {Premises} from "./premises";
import {Claims} from "./claims";
import {ExportToExcel} from "./export-to-excel";
import {isEmptyObject} from "devextreme/core/utils/type";


const api_host = "http://localhost:5000"

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
            fileId: 3
        };

        // bindings in order to pass functions to child "file-upload.jsx"
        this.adjustInputFile = this.adjustInputFile.bind(this);
        this.tagWithFile = this.tagWithFile.bind(this);

    }

    adjustInputText(event) {
        this.setState({inputText: event.target.value}, () => console.log("setting new text:", this.state.inputText)); // TODO
    }

    adjustInputFile(event) {
        if (event.target.files.length > 0) {
            this.setState({inputFile: event.target.files[0]}, () => console.log("setting new file:", this.state.inputFile.name)); // TODO
        }
    }

    tagWithText() {
        const {inputText} = this.state;
        console.log("tagging input text", inputText); // TODO
        const request_url = `${api_host}/api/tagWithText`
        axios.post(request_url, {"text": inputText})
            .then((response) => {
                console.log(response.status); // TODO

                this.setState({resultJSON: response.data})
                this.setState({fileId: this.state.resultJSON.id})
                this.setState({claims: this.state.resultJSON.claims})
                this.setState({premises: this.state.resultJSON.premises})
                this.setState({blocks: this.state.resultJSON.blocks})
            })
            .catch((err) => {
                console.log("error during request:", request_url, "\n", err);
                alert(`Something went wrong!\nError during request: ${request_url}`);
            });
    }

    tagWithFile() {
        // for file upload tutorial, see https://www.nicesnippets.com/blog/react-js-file-upload-example-with-axios
        const {inputFile} = this.state;
        console.log("checking input file\n", inputFile); // TODO

        if (inputFile) {
            // Create an object of formData
            const formData = new FormData();

            // Update the formData object
            formData.append("file", inputFile);
            console.log(formData); // TODO

            // Request made to the backend api to send formData object
            const request_url = `${api_host}/api/tagWithFile`
            axios.post(request_url, formData)
                .then((response) => {
                    console.log(response.data); // TODO
                    console.log(response.status); // TODO
                    this.setState({resultJSON: response.data})
                    this.setState({fileId: this.state.resultJSON.id})
                    this.setState({claims: this.state.resultJSON.claims})
                    this.setState({premises: this.state.resultJSON.premises})
                    this.setState({blocks: this.state.resultJSON.blocks})
                })
                .catch((err) => {
                    console.log("error during request:", request_url, "\n", err);
                    alert(`Something went wrong!\nError during request: ${request_url}`);
                });
        }
    }

    showTaggedFulltext() {
        // console.log("is resultJSON empty?:", isEmptyObject(this.state.resultJSON))
        if (!(isEmptyObject(this.state.blocks))) {
            const text_array = [];
            // console.log("First element in resultJSON.blocks", this.state.resultJSON.blocks[0])
            for (const block of this.state.blocks) {
                for (const word_obj of block) {
                    console.log("object", word_obj)
                    const classes = `block-text ${word_obj.label === "C" ? "block-claim" : (word_obj.label === "P" ? "block-premise" : "")}`;
                    // console.log("premise / text / claim: ", classes, word.token)
                    // console.log("block keys: "+ Object.keys(word_obj))
                    const idx = word_obj.idx;
                    console.log("word index: " + idx)
                    const html = (
                        <span className={classes} id={idx}>{word_obj.token + " "}</span>

                    );
                    text_array.push(html);
                }
            }
            return text_array;
        }
    }

    render() {
        const renderResultSection = () => {
            if (isEmptyObject(this.state.blocks)) {
                return <div> </div>;
            } else {
                return <div>
                    <h4 className="section-title">2. Results</h4>
                    <div className={"miner-results"}>
                        <div className={"miner-results-list"}>
                            <div className={"miner-results-claims"}>
                                <h5>Claims</h5>
                                <Claims claims={this.state.claims}/>
                            </div>
                            <div className={"miner-results-arguments"}>
                                <h5>Premises</h5>
                                <Premises
                                    premises={this.state.premises}/>
                            </div>
                        </div>
                        <div> {this.showTaggedFulltext()} </div>
                        <ExportToExcel
                            fileId={this.state.fileId}
                            api_host = {api_host}/>
                    </div>
                    <br/>
                </div>;
            }
        }
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
                        <button onClick={this.tagWithText.bind(this)}>Start Tagging</button>
                    </div>
                    <FileUpload className="section section-file-upload"
                                tagWithFile={this.tagWithFile}
                                adjustInputFile={this.adjustInputFile}
                                inputFile={this.state.inputFile}
                    />
                </div>

                <br />
                {/*TODO: refactor to remove br tags and properly style hr*/}
                <hr className="solid" style={{position: "relative", top: "1em"}} />
                <br />
                {renderResultSection()}
            </div>
        );
    }
}
