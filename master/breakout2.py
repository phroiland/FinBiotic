#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:17:12 2017

@author: jonfroiland
"""

#from decimal import Decimal
import pandas as pd
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)

class StreamingData(object):
    def __init__(self, time, mid, api, _id, xsec, xmin):
        self.time = time
        self.mid = mid
        self.api = api
        self._id = _id
        self.xsec = xsec
        self.xmin = xmin
        self.data = self.resample(self.df())
        self.balance = self.balance()
        
    def balance(self):
        response = self.api.account.summary(self._id)
        keys = response.get("account").__dict__.keys()
        values = response.get("account").__dict__.values()
        details = zip(keys,values)
        balance = round(details[17][1],2)
        return balance
    
    def df(self):
        df1 = pd.DataFrame({'Time':[self.time]})
        df2 = pd.DataFrame({'Mid':[float(self.mid)]})
        df3 = pd.concat([df1,df2],axis=1,join='inner')
        df3 = df3.set_index(['Time'])
        df3.index = pd.to_datetime(df3.index,unit='s')
        return df3
    
    def resample(self, df):
        xx = df.to_period(freq=self.xsec)
        openCol = xx.resample(self.xmin).first()
        highCol = xx.resample(self.xmin).max()
        lowCol = xx.resample(self.xmin).min()
        closeCol = xx.resample(self.xmin).last()
        self.data = pd.concat([openCol,highCol,lowCol,closeCol],
                               axis=1,join='inner')
        self.data['Open'] = openCol.round(5)
        self.data['High'] = highCol.round(5)
        self.data['Low'] = lowCol.round(5)
        self.data['Close'] = closeCol.round(5)
        self.data['20 High Close'] = self.data['Close'].rolling(20).max()
        self.data['20 Low Close'] = self.data['Close'].rolling(20).min()
        self.data['Other High Close'] = self.data['Close'].rolling(10).max()
        self.data['Other Low Close'] = self.data['Close'].rolling(18).min()
        self.data['HL'] = self.data['High']-self.data['Low']
        self.data['HC'] = self.data['High']-self.data['Close']
        self.data['CL'] = self.data['Close']-self.data['Low']
        self.data['True Range'] = \
        self.data[['HL','HC','CL']].max(axis=1).round(5)
        try:
            self.data['N'] = self.data['True Range'].rolling(20).mean().round(5)
            self.data['$Volatility'] = self.data['N']*self.data['Close']*50
        except:pass
        self.data['Account'] = self.balance
        try:
            self.data['Lot Size'] = \
            self.data['Account']/self.data['$Volatility']
            self.data['Lot Size'] = self.data['Lot Size'].fillna(0.0).astype(int)
        except:pass
        return self.data
    
    def minuteData(self):
        minuteData = self.data[['Open','High','Low','Close',
                                '20 High Close','Other High Close',
                                '20 Low Close','Other Low Close','True Range',
                                'N','$Volatility','Lot Size']]
        return minuteData
    
    
"""

class Breakout:
    
    def __init__(self, api, account_id, data, price, instrument):
        self.api = api
        self.account_id = account_id
        self.data = data
        self.price = price
        self.instrument = instrument
        
    def side(self, data, instrument):
        self.data = data
        self.instrument = instrument
        if (
                data.shape[0]>19 and \
                data['High'][-1]>data['20 High Close'][-2] and \
                data.iloc[0]['TradeID'] is None
            ):
            units = data['Lot Size'][-1].astype('str')
            return units, instrument
        elif (
                data.shape[0]>19 and \
                data['High'][-1]<data['20 High Close'][-2] and \
                data.iloc[0]['TradeID'] is None
            ):
            units = int(data['Lot Size'][-1].astype('str'))*-1
            return units, instrument
    
    def profit(self, data, price, instrument):
        self.data = data
        self.price = price
        self.instrument = instrument
        if (
                Decimal(price)>=data.iloc[0]['Profit'] and \
                data.iloc[0]['Long'] is not None
            ):
            tradeID = data.iloc[0]['TradeID'],
            return price, instrument, tradeID
        elif (
                Decimal(price)<=data.iloc[0]['Profit'] and \
                data.iloc[0]['Short'] is not None
            ):
            tradeID = data.iloc[0]['TradeID'],
            return price, instrument, tradeID
    
    def stop_loss(self, data, instrument):
        self.data = data
        self.instrument = instrument
        if (
                data.shape[0]>19 and \
                data['High'][-1]>data['18 High Close'][-2] and \
                data.iloc[0]['Short'] is not None
            ):
            price = data['High'][-1].astype('str')
            tradeID = data.iloc[0]['TradeID']
            return price, instrument, tradeID
        elif (
                data.shape[0]>19 and \
                data['Low'][-1]<data['18 Low Close'][-2] and \
                data.iloc[0]['Long'] is not None
            ):
            price = data['Low'][-1].astype('str')
            tradeID = data.iloc[0]['TradeID']
            return price, instrument, tradeID
    
class Response:
    
    def __init__(self, api, account_id, data, price, 
                 instrument, units, tradeID, _long, short):
        self.api = api
        self.account_id = account_id
        self.data = data
        self.price = price
        self.instrument = instrument
        self.units = units
        self.tradeID = tradeID
        self.side = side
    
    def trade(self, api, account_id, data, instrument, units):
        self.api = api
        self.account_id = account_id
        self.data = data
        self.instrument = instrument 
        self.units = units
        response = api.order.market(
            account_id, instrument=instrument, units=units
        )
        tradeID = response.get('lastTransactionID')
        keys = response.get('orderFillTransaction').__dict__.keys()
        values = response.get('orderFillTransactions').__dict__.values()
        orderFill = zip(keys,values)
        profit = Decimal(orderFill[6][1] + .001)
        #
        # Process the response
        #
        print("Response: {} ({})".format(
                response.status,response.reason))
        print("")
        print_order_create_response_transactions(response)
        
        return 
"""



    
    
            
            
            
            
            
            