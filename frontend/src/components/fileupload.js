import React from "react";
import axios from "axios";

export class FileUpload extends React.Component {
    constructor() {
        super();
        this.state = {
            // Initially, no file is selected
            selectedFile: null
        };
    }

    // On file select (from the pop up)
    onFileChange = (event) => {
        // Update the state
        this.setState({selectedFile: event.target.files[0]});
    };

    // On file upload (click the upload button)
    onFileUpload = () => {
        // Create an object of formData
        const formData = new FormData();

        // Update the formData object
        formData.append("myFile", this.state.selectedFile, this.state.selectedFile.name);

        // Details of the uploaded file
        console.log(this.state.selectedFile);

        // Request made to the backend api
        // Send formData object
        axios.post("api/uploadfile", formData);
    };

    // File content to be displayed after
    // file upload is complete
    fileData = () => {
        if (this.state.selectedFile) {
            return (
                <div>
                    <h2 className={"section"}>File Details:</h2>

                    <p className={"section"}>File Name: {this.state.selectedFile.name}</p>

                    <p className={"section"}>File Type: {this.state.selectedFile.type}</p>

                    <p className={"section"}>Last Modified: {this.state.selectedFile.lastModifiedDate.toDateString()}</p>
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
            <div style={{marginLeft:"10%"}}>
                <h3 className={"section"}>Or browse a file of your computer</h3>
                <div>
                    <input type="file" onChange={this.onFileChange} />
                    <button onClick={this.onFileUpload}>Upload!</button>
                </div>
                {this.fileData()}
            </div>
        );
    }
}
