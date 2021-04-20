import React from "react";

export class DragAndDrop extends React.Component {
    constructor() {
        super();
        this.state = {
            dragging: false,
        };
    }

    dropRef = React.createRef();

    handleDrag = (e) => {
        // prevents the default behavior of the browser when something is dragged in or dropped (e.g. open the file )
        e.preventDefault();
        // stops the event from being propagated through parent and child elements
        e.stopPropagation();
    };

    handleDragIn = (e) => {
        // prevents the default behavior of the browser when something is dragged in or dropped (e.g. open the file )
        e.preventDefault();
        // stops the event from being propagated through parent and child elements
        e.stopPropagation();
        // want to keep track of the how many elements deep our cursor is, and only set call this.setState({dragging: false}) once our cursor is all the way out
        this.dragCounter++;

        if (e.dataTransfer.items && e.dataTransfer.items.length > 0) {
            this.setState({dragging: true});
        }
    };

    handleDragOut = (e) => {
        // prevents the default behavior of the browser when something is dragged in or dropped (e.g. open the file )
        e.preventDefault();
        // stops the event from being propagated through parent and child elements
        e.stopPropagation();

        // // want to keep track of the how many elements deep our cursor is, and only set call this.setState({dragging: false}) once our cursor is all the way out
        this.dragCounter--;
        if (this.dragCounter > 0) return;

        this.setState({dragging: false});
    };

    handleDrop = (e) => {
        // prevents the default behavior of the browser when something is dragged in or dropped (e.g. open the file )
        e.preventDefault();
        // stops the event from being propagated through parent and child elements
        e.stopPropagation();

        // hide the overlay,
        // check that there are indeed some files included,
        // pass the array to our callback,
        // clear the dataTransfer array,
        // and reset the drag counter
        this.setState({drag: false});
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            this.props.handleDrop(e.dataTransfer.files);
            e.dataTransfer.clearData();
            this.dragCounter = 0;
        }
    };

    componentDidMount() {
        this.dragCounter = 0;
        let div = this.dropRef.current;
        div.addEventListener("dragenter", this.handleDragIn);
        div.addEventListener("dragleave", this.handleDragOut);
        div.addEventListener("dragover", this.handleDrag);
        div.addEventListener("drop", this.handleDrop);
    }

    componentWillUnmount() {
        let div = this.dropRef.current;
        div.removeEventListener("dragenter", this.handleDragIn);
        div.removeEventListener("dragleave", this.handleDragOut);
        div.removeEventListener("dragover", this.handleDrag);
        div.removeEventListener("drop", this.handleDrop);
    }

    render() {
        return (
            <div style={{display: "inline-block", position: "relative"}} ref={this.dropRef}>
                {this.state.dragging && (
                    <div
                        style={{
                            border: "dashed grey 4px",
                            backgroundColor: "rgba(255,255,255,.8)",
                            position: "absolute",
                            top: 0,
                            bottom: 0,
                            left: 0,
                            right: 0,
                            zIndex: 10,
                        }}
                    >
                        <div
                            style={{
                                position: "absolute",
                                top: "50%",
                                right: 0,
                                left: 0,
                                textAlign: "center",
                                color: "grey",
                                fontSize: 36,
                            }}
                        >
                            <div>Let me go :)</div>
                        </div>
                    </div>
                )}
                {this.props.children}
            </div>
        );
    }
}
