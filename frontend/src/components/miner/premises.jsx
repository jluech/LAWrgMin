import React from "react";
import {Link} from "react-scroll";
import List from "devextreme-react/list";
import "devextreme/dist/css/dx.common.css";
import "devextreme/dist/css/dx.light.css";

export class Premises extends React.Component {
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

    itemTemplate(data) {
        // specify values which should be taken for the listing
        // data comes from dataSource={} in HTML part
        return (
            <Link className={"result-list-premise"}
                to={`premise-${data.idx}`}
                activeClass="active"
                spy={true}
                smooth={true}
            >{data.premise}</Link>
        );
    }

    createPremiseList() {
        const {premises} = this.props;
        const premise_list = [];
        if (premises.length > 0) {
            for (const premise of premises) {
                premise_list.push({"premise": premise["text"].trim(), "idx": premise["idx"]});
            }
        }
        return premise_list;
    }

    render() {
        return (
            <div className="list-container">
                <List
                    dataSource={this.createPremiseList()}
                    height={400}
                    itemRender={this.itemTemplate}
                    searchExpr="premise"
                    searchEnabled={true}
                    searchMode={this.state.searchMode}
                />
            </div>
        );
    }
}
