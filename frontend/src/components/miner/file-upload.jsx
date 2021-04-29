import React from "react";

export class FileUpload extends React.Component {
    constructor(props) {
        super(props);
    }

    // File content to be displayed after file upload is complete
    buildFileDataHtml = () => {
        if (this.props.inputFile) {
            return (
                <div>
                    <h2 className={"section"}>File Details:</h2>
                    <p className={"section"}>File Name: {this.props.inputFile.name}</p>
                    <p className={"section"}>File Type: {this.props.inputFile.type}</p>
                </div>
            );
        } else {
            return (
                <div>
                    <br />
                    <h4 className={"section"}>Choose before Pressing the Upload button</h4>
                </div>
            );
        }
    };

    render() {
        return (
            <div className={"upload-wrapper"}>
                <h3 className={"section"}>Or browse a PDF on your computer</h3>
                <div className={"upload-input"}>
                    <input type="file" onChange={this.props.adjustInputFile} />
                    <button onClick={this.props.tagWithFile}>Upload!</button>
                </div>
                {this.buildFileDataHtml()}
            </div>
        );
    }
}
