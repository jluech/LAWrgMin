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
        return <a href={`#${data.idx}`} className={"result-list-claims"}>{data.claim}</a>;
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevProps !== this.props) {
            this.createClaimList();
        }
    }

    createClaimList() {
        const claim_list = [];
        //console.log(this.props.claims);
        if (this.props.claims.length > 0) {
            for (const claim of this.props.claims) {
                let claim_words = "";
                const start_idx = claim[0]["idx"];

                for (const token_obj of claim) {
                    const token = token_obj["token"];
                    claim_words += this.determine_delimiter(token) + token;
                }
                claim_words = claim_words.trim();
                claim_list.push({"claim": claim_words, "idx": start_idx});
            }
            // console.log(claim_list); // TODO
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
                            height={400}
                            itemRender={this.itemTemplate}
                            searchExpr="claim"
                            searchEnabled={true}
                            searchMode={this.state.searchMode}
                        />
                    </div>
                </React.Fragment>
            </div>
        );
    }
}
