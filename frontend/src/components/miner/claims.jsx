import React from "react";
import {Link} from "react-scroll";
import List from "devextreme-react/list";
import "devextreme/dist/css/dx.common.css";
import "devextreme/dist/css/dx.light.css";

export class Claims extends React.Component {
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
            <Link className={"result-list-claim"}
                to={`claim-${data.idx}`}
                activeClass="active"
                spy={true}
                smooth={true}
            >{data.claim}</Link>
        );
    }

    createClaimList() {
        const claim_list = [];
        const {claims} = this.props;
        if (claims.length > 0) {
            for (const claim of claims) {
                claim_list.push({"claim": claim["text"].trim(), "idx": claim["idx"]});
            }
        }
        return claim_list;
    }

    render() {
        return (
            <div className="list-container">
                <List
                    dataSource={this.createClaimList()}
                    height={400}
                    itemRender={this.itemTemplate}
                    searchExpr="claim"
                    searchEnabled={true}
                    searchMode={this.state.searchMode}
                />
            </div>
        );
    }
}
