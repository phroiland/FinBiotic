import React from 'react';

export default class ModifyCurrencyPair extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            CurrencyPairName: props.CurrencyPair.CurrencyPairName,
            Website:props.CurrencyPair.Website,
            PairID: props.CurrencyPair.PairID,
            Password:props.CurrencyPair.Password
        };
    }

    handleCurrencyPairNameChange(e) {}

    handleWebsiteChange(e) {
        this.setState({
            Website: e.target.value
        });
    }

    handlePairIDChange(e) {
        this.setState({
            PairID: e.target.value
        });
    }

    handlePasswordChange(e) {
        this.setState({
            Password: e.target.value
        });
    }

    handleSubmit() {

     var currencyPair = {
             CurrencyPairName: this.state.CurrencyPairName,
             Website: this.state.Website,
             PairID: this.state.PairID,
             Password: this.state.Password
        };

        this.props.OnSubmit(currencyPair);
    }

    isUserEntryValid() {
         return true;
    }

    render() {
          return(<form>
                    <div className="form-group">
                        <label htmlFor="currencyPairName">CurrencyPair Name</label>
                        <input type="text" className="form-control" id="currencyPairName" placeholder="CurrencyPair Name"
                               disabled="true"  onChange={this.handleCurrencyPairNameChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="website">Website</label>
                        <input type="text" className="form-control" id="website" placeholder="Website"
                                 onChange={this.handleWebsiteChange.bind(this)}  />
                    </div>
                    <div className="form-group">
                        <label htmlFor="PairID">User Id</label>
                        <input type="text" className="form-control" id="PairID" placeholder="User Name"
                                onChange={this.handlePairIDChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="text" className="form-control" id="password" placeholder="Password Name"
                               onChange={this.handlePasswordChange.bind(this)}  />
                    </div>
                    <button type="button" className="btn btn-default" onClick={() => this.handleSubmit()}>Submit</button>
                </form>);
    }
}