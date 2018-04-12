import React from 'react';
export default class MarketList extends React.Component {
    constructor(props) {
        super(props);
    }

    handleButtonClickEdit(market) {
        this.props.OnEdit(market);
    }

    handleButtonClickDelete(market) {
        this.props.OnDelete(market);
    }

    render() {
        return(<table className="table table-stripped">
            <thead>
                <tr>
                    <th>Market</th>
                    <th>Units</th>
                    <th>Order Type</th>
                    <th>Entry Price</th>
                    <th>Stop Loss</th>
                    <th>Take Profit</th>
                    <th>Current Price</th>
                    <th>Profit (Loss)</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {
                this.props.Markets.map((market) =>
                    <tr key={market.MarketName}>
                        <td><a href={market.Chart}>{market.MarketName}</a></td>
                        <td>{market.Units}</td>
                        <td>{market.OrderType}</td>
                        <td>{market.EntryPrice}</td>
                        <td>{market.StopLoss}</td>
                        <td>{market.TakeProfit}</td>
                        <td>{market.CurrentPrice}</td>
                        <td>{market.ProfitLoss}</td>
                        <td><button type="button" className="btn btn-primary" onClick={() => this.handleButtonClickEdit(market)}>
                            <span className="glyphicon glyphicon-pencil" aria-hidden="true"></span>
                            </button>
                            &nbsp;&nbsp;
                            <button type="button" className="btn btn-primary" onClick={() => this.handleButtonClickDelete(market)}>
                                <span className="glyphicon glyphicon-remove" aria-hidden="true"></span>
                            </button>
                        </td>
                    </tr>)
                }
            </tbody>
        </table>
        );
    }
}
