import React from "react";
import axios from "axios";

export class FileUpload extends React.Component {
    constructor(props) {
        super(props);
    }

    // On file upload (click the upload button)
    onFileUpload = () => {
        const {selectedFile} = this.state;

        if (selectedFile) {
            // Create an object of formData
            const formData = new FormData();

            // Update the formData object
            formData.append("myFile", selectedFile, selectedFile.name);

            // Details of the uploaded file
            console.log(this.state.selectedFile);

            // Request made to the backend api to send formData object
            axios.post("api/uploadfile", formData);
        }
    };

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
