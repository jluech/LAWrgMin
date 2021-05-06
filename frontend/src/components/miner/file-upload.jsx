import React from "react";
import Button from "react-bootstrap/Button";

export class FileUpload extends React.Component {

    // File content to be displayed after file upload is complete
    buildFileDataHtml = () => {
        if (this.props.inputFile) {
            return <div>File name: {this.props.inputFile.name}</div>;
        } else {
            return <div className={"upload-warning"}>Choose a PDF or Word document first!</div>;
        }
    };

    render() {
        return (
            <div className={"upload-wrapper"}>
                <h3 className={"section"}>Or browse a file on your computer</h3>
                <div className={"upload-input"}>
                    <input type="file" onChange={this.props.adjustInputFile} />
                </div>
                <div className={"section upload-section"}>
                    {this.buildFileDataHtml()}
                    <Button variant="outline-light"
                            onClick={(event) => this.props.tagWithFile(event)}
                    >Start Tagging</Button>
                </div>
            </div>
        );
    }
}
