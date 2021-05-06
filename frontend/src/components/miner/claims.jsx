import React from "react";
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

    itemTemplate(data) {
        // specify values which should be taken for the listing
        // data comes from dataSource={} in HTML part
        return <a href={`#claim-${data.idx}`} className={"result-list-claim"}>{data.claim}</a>;
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

    onSearchModeChange(args) {
        this.setState({
            searchMode: args.value,
        });
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
