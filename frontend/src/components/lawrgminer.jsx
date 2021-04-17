import React from 'react';
import {FileUpload} from "./fileupload";
import {DragAndDrop} from "./draganddrop";



export class Lawrgminer extends React.Component {

    constructor() {
        super();
        this.state = {
            files: [
                'testfile.pdf'
            ]
        }
    }

    handleDrop = (files) => {
        let fileList = this.state.files
        for (let i = 0; i < files.length; i++) {
            if (!files[i].name) return
            fileList.push(files[i].name)
        }
        this.setState({files: fileList})
    }

    render() {
        return <div id='lawrgminer' style={{backgroundColor:'lightgray'}}>
            <h2 id='introduction' className="section">I am the LAWrgMiner</h2>
            <h3 className="section">Argumentation Mining in Law</h3>
            <div >
                <h4 className='section'>1. Text Input</h4>
                <hr className="solid" style={{position:'relative', top:'1em', left:'3em'}}/>

                <DragAndDrop handleDrop={this.handleDrop} >
                    <div className='section' style={{height: 300, width: 250}}>
                        {
                            this.state.files.map((file) =>
                            <div key={this.i}>
                                {file}
                            </div>
                        )}
                    </div>
                </DragAndDrop>
                <FileUpload/>

            </div>
        </div>;
    }
}

