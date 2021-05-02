import React from "react";
import List from "devextreme-react/list";
import "devextreme/dist/css/dx.common.css";
import "devextreme/dist/css/dx.light.css";

function ItemTemplate(data) {
    return <div>{data.claim}</div>;
}

export class Claims extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            searchMode: "contains",

        };
        this.onSearchModeChange = this.onSearchModeChange.bind(this);
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevProps !== this.props) {
            this.createClaimList();
        }
    }

    createClaimList() {
        const claim_list = [];
        console.log(this.props.claims); // TODO
        if (this.props.claims.length > 0) {
            for (const claim of this.props.claims) {
                let claim_words = "";
                for (const token_obj of claim) {
                    const token = token_obj["token"];
                    claim_words += this.determine_delimiter(token) + token;
                }
                claim_words = claim_words.trim();
                claim_list.push({"claim": claim_words});
            }
            console.log(claim_list); // TODO
        }
        return claim_list;
    }

    determine_delimiter(token) {
        if (token.length > 1) {
            return " ";
        }
        if (token.toLowerCase().match(/^([0-9]|[a-z])+([0-9a-z]+)$/i) || ["(", "{"].includes(token)) {
            return " ";
        }
        return "";
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
                            dataSource={this.createClaimList()}
                            height={600}
                            itemRender={ItemTemplate}
                            searchExpr="p"
                            searchEnabled={true}
                            searchMode={this.state.searchMode}
                        />
                    </div>
                </React.Fragment>
            </div>
        );
    }
}
