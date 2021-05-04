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
                    <br/>
                    <p className={"section"}>File name: {this.props.inputFile.name}</p>
                </div>
            );
        } else {
            return (
                <div>
                    <br />
                    <h4 className={"section"}>Choose a PDF before pressing the Tagging button</h4>
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
                </div>
                {this.buildFileDataHtml()}
                <button onClick={(event) => this.props.tagWithFile(event)}>Start Tagging</button>
            </div>
        );
    }
}
