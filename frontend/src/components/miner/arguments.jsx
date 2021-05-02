import React from "react";
import List from "devextreme-react/list";
import "devextreme/dist/css/dx.common.css";
import "devextreme/dist/css/dx.light.css";

function ItemTemplate(data) {
    // specify values which should be taken for the listing
    // data comes from dataSource={} in HTML part
    return <div>{data.Name}</div>;
}

export class Arguments extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            searchMode: "contains",
        };
        this.onSearchModeChange = this.onSearchModeChange.bind(this);
    }

    onSearchModeChange(args) {
        this.setState({
            searchMode: args.value,
        });
    }

    render() {
        return (
            <div>
                <React.Fragment>
                    <div className="list-container">
                        <List
                            dataSource={this.props.lawrgminerTags}
                            height={600}
                            itemRender={ItemTemplate}
                            searchExpr="Name"
                            searchEnabled={true}
                            searchMode={this.state.searchMode}
                        />
                    </div>
                </React.Fragment>
            </div>
        );
    }
}
