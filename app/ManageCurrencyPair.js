import React from 'react'
import ReactDOM from 'react-dom'
import CurrencyPairList from './CurrencyPairList.js';
import NewCurrencyPair from './NewCurrencyPair.js';
import FilterAndAdd from './Filter.js';
import ModifyCurrencyPair from './ModifyCurrencyPair.js';
export default class ManageCurrencyPairs extends React.Component {

    constructor(props) {
        super(props);

        //Create a Local Storage Item to hold list of CurrencyPairs, if it does not already exist
        if (localStorage.getItem('CurrencyPairList') === null)
        {
            //initialize the Local Storage with an empty array
            localStorage.setItem('CurrencyPairList',JSON.stringify([]));
        }

        //Define the Initial State of the Application
        this.state = {
            ShowNewCurrencyPairUI : false,
            ShowModifyCurrencyPairUI: false,
            ShowCurrencyPairList : true,
            ShowFilterUI: true,
            CurrencyPairList: JSON.parse(localStorage.getItem('CurrencyPairList'))
        }
    }

    filterCurrencyPairList(filter) {
        var newCurrencyPairList = JSON.parse(localStorage.getItem("CurrencyPairList")).filter(function(currencyPair) {
            return currencyPair.CurrencyPairName.includes(filter);
        });

        this.setState({
            CurrencyPairList: newCurrencyPairList,
        });
    }

    addNewCurrencyPair(currencyPair) {
        var currencyPairList = JSON.parse(localStorage.getItem('CurrencyPairList'));
        currencyPairList.push(currencyPair);
        localStorage.setItem("CurrencyPairList",JSON.stringify(currencyPairList));

        this.setState({
            ShowNewCurrencyPairUI : false,
            ShowModifyCurrencyPairUI: false,
            ShowCurrencyPairList : true,
            ShowFilterUI : true,
            CurrencyPairList: JSON.parse(localStorage.getItem('CurrencyPairList'))
        });

    }

    modifyCurrencyPair(currencyPairToModify) {
        var currencyPairList = JSON.parse(localStorage.getItem('CurrencyPairList'));
        var index = currencyPairList.findIndex(function(currencyPair) {
            return currencyPairToModify.CurrencyPairName === currencyPair.CurrencyPairName;
        });

        if (index != -1)
        {
            currencyPairList[index].CurrencyPairName = currencyPairToModify.CurrencyPairName;
            currencyPairList[index].Website = currencyPairToModify.Website;
            currencyPairList[index].PairID = currencyPairToModify.PairID;
            currencyPairList[index].Password = currencyPairToModify.Password;
        }

        localStorage.setItem('CurrencyPairList',JSON.stringify(currencyPairList));

        this.setState({
            ShowNewCurrencyPairUI : false,
            ShowModifyCurrencyPairUI: false,
            ShowCurrencyPairList : true,
            ShowFilterUI : true,
            CurrencyPairList: JSON.parse(localStorage.getItem('CurrencyPairList'))
        });
    }

    removeCurrencyPair(currencyPairToRemove) {
        var result = confirm("Are you sure you want to remove the currencyPair");
        if (result == false)
        return;
        var currencyPairList = JSON.parse(localStorage.getItem("CurrencyPairList"))

        var newCurrencyPairList = currencyPairList.filter(function(currencyPair) {
            return currencyPair.CurrencyPairName != currencyPairToRemove.CurrencyPairName
        });
        localStorage.setItem("CurrencyPairList", JSON.stringify(newCurrencyPairList));

        this.setState( {
            CurrencyPairList: JSON.parse(localStorage.getItem('CurrencyPairList'))
        });
    }

    render() {
        return(
        <div>
            {this.state.ShowFilterUI && <FilterAndAdd OnAdd={this.showNewCurrencyPairScreen.bind(this)} OnFilter={this.filterCurrencyPairList.bind(this)} />}
            {this.state.ShowCurrencyPairList &&  <CurrencyPairList CurrencyPairs={this.state.CurrencyPairList} OnEdit={this.showModifyCurrencyPairScreen.bind(this)} OnDelete={this.removeCurrencyPair.bind(this)}  /> }
            {this.state.ShowNewCurrencyPairUI &&  <NewCurrencyPair OnSubmit={this.addNewCurrencyPair.bind(this)} />}
            {this.state.ShowModifyCurrencyPairUI && <ModifyCurrencyPair CurrencyPair={this.state.CurrencyPairToBeModified} OnSubmit={this.modifyCurrencyPair.bind(this)} />}
        </div>);
    }

    showModifyCurrencyPairScreen(currencyPairToModify) {
        this.setState({
            ShowModifyCurrencyPairUI : true,
            ShowCurrencyPairList : false,
            ShowFilterUI: false,
            CurrencyPairToBeModified:currencyPairToModify
        })
    }

    showNewCurrencyPairScreen() {
        this.setState({
            ShowNewCurrencyPairUI : true,
            ShowCurrencyPairList: false,
            ShowFilterUI: false
        })
    }
}