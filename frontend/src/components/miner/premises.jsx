import React from "react";
import List from "devextreme-react/list";
import "devextreme/dist/css/dx.common.css";
import "devextreme/dist/css/dx.light.css";

function ItemTemplate(data) {
    // specify values which should be taken for the listing
    // data comes from dataSource={} in HTML part
    return <div>{data.premise}</div>;
}

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

    componentDidUpdate(prevProps, prevState) {
        if (prevProps !== this.props) {
            this.createPremiseList();
        }
    }

    createPremiseList() {
        const premise_list = [];
        console.log(this.props.premises); // TODO
        if (this.props.premises.length > 0) {
            for (const premise of this.props.premises) {
                let premise_words = "";
                for (const token_obj of premise) {
                    const token = token_obj["token"];
                    premise_words += this.determine_delimiter(token) + token;
                }
                premise_words = premise_words.trim();
                premise_list.push({"premise": premise_words});
            }
            console.log(premise_list); // TODO
        }
        return premise_list;
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

    render() {
        return (
            <div>
                <React.Fragment>
                    <div className="list-container">
                        <List
                            dataSource={this.createPremiseList()}
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
