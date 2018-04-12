import React from 'react';

export default class NewMarket extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            MarketName: '',
            Chart: '',
            Units: '',
            OrderType: '',
            EntryPrice: '',
            StopLoss: '',
            TakeProfit: '',
            CurrentPrice: '',
            ProfitLoss: ''
        };
    }


    handleMarketNameChange(e) {
        this.setState({
            MarketName: e.target.value
        });
    }

    handleChartChange(e) {
        this.setState({
            Chart: e.target.value
        });
}

    handleUnitsChange(e) {
        this.setState({
            Units: e.target.value
        });
    }

    handleOrderTypeChange(e) {
        this.setState({
            OrderType: e.target.value
        });
    }

    handleEntryPriceChange(e) {
        this.setState({
            EntryPrice: e.target.value
        });
    }

    handleStopLossChange(e) {
        this.setState({
            StopLoss: e.target.value
        });
    }

    handleTakeProfitChange(e) {
        this.setState({
            TakeProfit: e.target.value
        });
    }

    handleCurrentPriceChange(e) {
        this.setState({
            CurrentPrice: e.target.value
        });
    }

    handleProfitLossChange(e) {
        this.setState({
            ProfitLoss: e.target.value
        });
    }

    handleSubmit() {
        var market = {
            MarketName: this.state.MarketName,
            Chart: this.state.Chart,
            Units: this.state.Units,
            OrderType: this.state.OrderType,
            EntryPrice: this.state.EntryPrice,
            StopLoss: this.state.StopLoss,
            TakeProfit: this.state.TakeProfit,
            CurrentPrice: this.state.CurrentPrice,
            ProfitLoss: this.state.ProfitLoss,
        };
        this.props.OnSubmit(market);
    }

    render() {
        return(<form>
                    <div className="form-group">
                        <label htmlFor="marketName">Market Name</label>
                        <input type="text" className="form-control" id="marketName" placeholder="Market Name"
                                onChange={this.handleMarketNameChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="chart">Chart</label>
                        <input type="text" className="form-control" id="chart" placeholder="Chart"
                                onChange={this.handleChartChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="Units">Units</label>
                        <input type="text" className="form-control" id="Units" placeholder="Units"
                                onChange={this.handleUnitsChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="orderType">OrderType</label>
                        <input type="text" className="form-control" id="orderType" placeholder="OrderType"
                                 onChange={this.handleOrderTypeChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="entryPrice">EntryPrice</label>
                        <input type="text" className="form-control" id="entryPrice" placeholder="EntryPrice"
                                 onChange={this.handleEntryPriceChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="stopLoss">StopLoss</label>
                        <input type="text" className="form-control" id="stopLoss" placeholder="StopLoss"
                                 onChange={this.handleStopLossChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="takeProfit">TakeProfit</label>
                        <input type="text" className="form-control" id="takeProfit" placeholder="TakeProfit"
                                 onChange={this.handleTakeProfitChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="currentPrice">CurrentPrice</label>
                        <input type="text" className="form-control" id="currentPrice" placeholder="CurrentPrice"
                                 onChange={this.handleCurrentPriceChange.bind(this)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="profitLoss">ProfitLoss</label>
                        <input type="text" className="form-control" id="profitLoss" placeholder="ProfitLoss"
                                 onChange={this.handleProfitLossChange.bind(this)} />
                    </div>
                    <button type="button" className="btn btn-default" onClick={() => this.handleSubmit()}>Submit</button>
                </form>);
    }
}
