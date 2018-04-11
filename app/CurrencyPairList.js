import React from 'react';
export default class CurrencyPairList extends React.Component {
    constructor(props) {
        super(props);
    }

    handleButtonClickEdit(currencyPair) {
        this.props.OnEdit(currencyPair);
    }

    handleButtonClickDelete(currencyPair) {
        this.props.OnDelete(currencyPair);
    }

    render() {
        return(<table className="table table-stripped">
            <thead>
                <tr>
                    <th>Currency Pair</th>
                    <th>Pair ID</th>
                    <th>Password</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {
                this.props.CurrencyPairs.map((currencyPair) =>
                    <tr key={currencyPair.CurrencyPairName}>
                        <td><a href={currencyPair.Website}>{currencyPair.CurrencyPairName}</a></td>
                        <td>{currencyPair.PairID}</td>
                        <td>{currencyPair.Password}</td>
                        <td><button type="button" className="btn btn-primary" onClick={() => this.handleButtonClickEdit(currencyPair)}>
                            <span className="glyphicon glyphicon-pencil" aria-hidden="true"></span>
                            </button>
                            &nbsp;&nbsp;
                            <button type="button" className="btn btn-primary" onClick={() => this.handleButtonClickDelete(currencyPair)}>
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