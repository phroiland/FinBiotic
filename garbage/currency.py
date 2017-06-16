#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 07:17:05 2017

@author: jonfroiland
"""

"""
    Be sure to include docstrings at the module, class, and method levels.
"""
"""
    The advantage of class definitions in general is to achieve code reuse via
    inheritance.
"""
import pandas as pd
from datetime import datetime
#from decimal import *
#getcontext().prec = 4

class Currency:
    
    def __init__(self, price):
        self.time = datetime.now(),
        self.instrument = price.instrument,
        self.bid = price.bids[0].price,
        self.ask = price.asks[0].price,
        
    
    def mid(price):
        mid = float((price.asks[0].price + price.bids[0].price)/2)
        return "{}".format(mid)
    
    
    def dataframes(self,time,mid):
        time = pd.DataFrame({'Time':[Currency().time]})
        mid = pd.DataFrame({'Mid':[Currency().mid()]})
        df = []
        df = df.concat([time,mid],axis=1,join='inner')



"""
class Breakout:
    
    def __init__(self, shape, high, high_close, low, low_close)
        self.shape = shape
        self.high = high,
        self.high_close = high_close,
        self.low = low,
        self.low_close = low_close
    
    def 
    
    
    def trade(instrument, price):
        if (
                minuteData.shape[0] > 19 and \
                minuteData['High'][-1] > minuteData['20 High Close'][-2] and \
                "Something to check unopened Oanda long positions" is None
            ): return positionL

        elif (
                minuteData.shape[0] > 19 and \
                minuteData['Low'][-1] < minuteData['20 Low Close'][-2] and \
                "Something to check open Oanda long positions" is not None
            ): return positionSL
        
        elif (
                minuteData.shape[0] > 19 and \
                minuteData['Low'][-1] < minuteData['20 Low Close'][-2] and \
                "Something to check unopened Oanda short positions" is None
            ): return positionS
                
        elif (
                minuteData.shape[0] > 19 and \
                minuteData['High'][-1] > minuteData['20 High Close'][-2] and \
                "Something to check open Oanda short positions" is not None
            ): return positionSS
        
        else: continue

class Euro(Currency):
    def price(self):
        return Decimal(self.price)

class Cable(Currency):
    def price(self):
        return Decimal(self.price)

class Loonie(Currency):
    def price(self):
        return Decimal(self.price)

class Swiss(Currency):
    def price(self):
        return Decimal(self.price)

class Kiwi(Currency):
    def price(self):
        return Decimal(self.price)

class Aussie(Currency):
    def price(self):
        return Decimal(self.price)

    The following is a class that will be used to build four positions.
        - Long
        - Stop Loss for Long
        - Short
        - Stop Loss for Short

class Position:
    def __init__(self,name, symbol):
        self.name = name,
        self.symbol = symbol

Long, stopLong, Short, stopShort = Position('Long','L'), 
Position('stopLong','SL'), Position('Short','S'), Position('stopShort','SS')

positionL = [Euro('EURUSD',Long),Cable('GPBUSD',Long),Loonie('USDCAD',Long),
             Swiss('USDCHF',Long),Kiwi('NZD/USD',Long),Aussie('AUDUSD',Long)]

positionSL = [Euro('EURUSD',stopLong),Cable('GPBUSD',stopLong),
               Loonie('USDCAD',stopLong),Swiss('USDCHF',stopLong),
               Kiwi('NZD/USD',stopLong),Aussie('AUDUSD',stopLong)]

positionS = [Euro('EURUSD',Short),Cable('GPBUSD',Short),Loonie('USDCAD',Short),
             Swiss('USDCHF',Short),Kiwi('NZD/USD',Short),Aussie('AUDUSD',Short)]
                                    
positionSS = [Euro('EURUSD',stopShort),Cable('GPBUSD',stopShort),
              Loonie('USDCAD',stopShort),Swiss('USDCHF',stopShort),
              Kiwi('NZD/USD',stopShort),Aussie('AUDUSD',stopShort)]




class Economics():
   
        Economic Releases
            
            Eurozone: 
                monthly economic data is generally released at 2 a.m. Eastern 
                Time (ET) in the United States. The time segment from 30 to 60 
                minutes prior to these releases and one to three hours after-
                wards highlights an enormously popular period to trade EUR 
                pairs because the news will impact at least three of the five 
                most popular crosses. It also overlaps the run-up into the U.S. 
                trading day, drawing in significant volume from both sides of 
                the Atlantic.

            USzone:
                U.S. economic releases tend to be released between 8:30 a.m. 
                and 10 a.m. ET and generate extraordinary EUR trading volume as 
                well, with high odds for strongly trending price movement in 
                the most popular pairs. Japanese data releases get less 
                attention because they tend to come out at 4:30 p.m. and 
                10 p.m. ET, when the eurozone is in the middle of their sleep 
                cycle. Even so, trading volume with the EUR/JPY and EUR/USD 
                pairs can spike sharply around these time zones.
        

    def __init__(self, zone, hours):
        self.zone = zone
        self.hours = hours
    
    def eurozone(self, instrument, hours):
    
    def uszone(self, instrument, hours):
"""