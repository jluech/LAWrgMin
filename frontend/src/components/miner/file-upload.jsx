import React from "react";
import {Button, Spinner} from "react-bootstrap";

export class FileUpload extends React.Component {

    // File content to be displayed after file upload is complete
    buildFileDataHtml = () => {
        if (!this.props.inputFile) {
            return <div className={"upload-warning"}>Choose a PDF or Word document first!</div>;
        }
    };

    render() {
        return (
            <div className={"upload-wrapper"}>
                <h3 className={"section"}>...or browse a file on your computer</h3>
                <div className={"upload-input"}>
                    <input type="file" onChange={this.props.adjustInputFile} ref={this.props.setRef} />
                </div>
                <div className={"section upload-section"}>
                    {this.buildFileDataHtml()}
                    <Button variant="outline-light"
                            onClick={(event) => this.props.tagWithFile(event)}
                    >
                        {this.props.isAwaitingFile ?
                            (<span className={"input-btn-text"}>
                                    <Spinner animation={"border"} size={"sm"} role={"status"}
                                             as={"span"}
                                    /><span>...Tagging</span>
                                </span>)
                            : (<span className={"input-btn-text"}>Start Tagging</span>)
                        }
                    </Button>
                </div>
            </div>
        );
    }
}
