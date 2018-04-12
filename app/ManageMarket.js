import React from 'react'
import ReactDOM from 'react-dom'
import MarketList from './MarketList.js';
import NewMarket from './NewMarket.js';
import FilterAndAdd from './Filter.js';
import ModifyMarket from './ModifyMarket.js';
export default class ManageMarkets extends React.Component {

    constructor(props) {
        super(props);

        //Create a Local Storage Item to hold list of Markets, if it does not already exist
        if (localStorage.getItem('MarketList') === null)
        {
            //initialize the Local Storage with an empty array
            localStorage.setItem('MarketList',JSON.stringify([]));
        }

        //Define the Initial State of the Application
        this.state = {
            ShowNewMarketUI : false,
            ShowModifyMarketUI: false,
            ShowMarketList : true,
            ShowFilterUI: true,
            MarketList: JSON.parse(localStorage.getItem('MarketList'))
        }
    }

    filterMarketList(filter) {
        var newMarketList = JSON.parse(localStorage.getItem("MarketList")).filter(function(market) {
            return market.MarketName.includes(filter);
        });

        this.setState({
            MarketList: newMarketList,
        });
    }

    addNewMarket(market) {
        var marketList = JSON.parse(localStorage.getItem('MarketList'));
        marketList.push(market);
        localStorage.setItem("MarketList",JSON.stringify(marketList));

        this.setState({
            ShowNewMarketUI : false,
            ShowModifyMarketUI: false,
            ShowMarketList : true,
            ShowFilterUI : true,
            MarketList: JSON.parse(localStorage.getItem('MarketList'))
        });

    }

    modifyMarket(marketToModify) {
        var marketList = JSON.parse(localStorage.getItem('MarketList'));
        var index = marketList.findIndex(function(market) {
            return marketToModify.MarketName === market.MarketName;
        });

        if (index != -1)
        {
            marketList[index].MarketName = marketToModify.MarketName;
            marketList[index].Chart = marketToModify.Chart;
            marketList[index].Units = marketToModify.Units;
            marketList[index].OrderType = marketToModify.OrderType;
            marketList[index].EntryPrice = marketToModify.EntryPrice;
            marketList[index].StopLoss = marketToModify.StopLoss;
            marketList[index].TakeProfit = marketToModify.TakeProfit;
            marketList[index].CurrentPrice = marketToModify.CurrentPrice;
            marketList[index].ProfitLoss = marketToModify.ProfitLoss;
        }

        localStorage.setItem('MarketList',JSON.stringify(marketList));

        this.setState({
            ShowNewMarketUI : false,
            ShowModifyMarketUI: false,
            ShowMarketList : true,
            ShowFilterUI : true,
            MarketList: JSON.parse(localStorage.getItem('MarketList'))
        });
    }

    removeMarket(marketToRemove) {
        var result = confirm("Are you sure you want to remove the market");
        if (result == false)
        return;
        var marketList = JSON.parse(localStorage.getItem("MarketList"))

        var newMarketList = marketList.filter(function(market) {
            return market.MarketName != marketToRemove.MarketName
        });
        localStorage.setItem("MarketList", JSON.stringify(newMarketList));

        this.setState( {
            MarketList: JSON.parse(localStorage.getItem('MarketList'))
        });
    }

    render() {
        return(
        <div>
            {this.state.ShowFilterUI && <FilterAndAdd OnAdd={this.showNewMarketScreen.bind(this)} OnFilter={this.filterMarketList.bind(this)} />}
            {this.state.ShowMarketList &&  <MarketList Markets={this.state.MarketList} OnEdit={this.showModifyMarketScreen.bind(this)} OnDelete={this.removeMarket.bind(this)}  /> }
            {this.state.ShowNewMarketUI &&  <NewMarket OnSubmit={this.addNewMarket.bind(this)} />}
            {this.state.ShowModifyMarketUI && <ModifyMarket Market={this.state.MarketToBeModified} OnSubmit={this.modifyMarket.bind(this)} />}
        </div>);
    }

    showModifyMarketScreen(marketToModify) {
        this.setState({
            ShowModifyMarketUI : true,
            ShowMarketList : false,
            ShowFilterUI: false,
            MarketToBeModified:marketToModify
        })
    }

    showNewMarketScreen() {
        this.setState({
            ShowNewMarketUI : true,
            ShowMarketList: false,
            ShowFilterUI: false
        })
    }
}
