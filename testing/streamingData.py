#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:17:12 2017

@author: jonfroiland
"""
import pandas as pd
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)

class StreamingData(object):
    def __init__(self, time, instrument, mid, api, _id, xsec, xmin, balance):
        self.time = time
        self.instrument = instrument
        self.mid = mid
        self.api = api
        self._id = _id
        self.xsec = xsec
        self.xmin = xmin
        self.balance = balance
        self.data = self.resample(self.df())
    
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
        try:
            self.data['Open'] = self.data['Open'].fillna(method='ffill')
            self.data['High'] = self.data['High'].fillna(method='ffill')
            self.data['Low'] = self.data['Low'].fillna(method='ffill')
            self.data['Close'] = self.data['Close'].fillna(method='ffill')
        except:pass
        self.data['20 High Close'] = self.data['Close'].rolling(20).max()
        self.data['20 Low Close'] = self.data['Close'].rolling(20).min()
        self.data['50 High Close'] = self.data['Close'].rolling(50).max()
        self.data['50 Low Close'] = self.data['Close'].rolling(50).min()
        self.data['HL'] = self.data['High']-self.data['Low']
        self.data['HC'] = self.data['High']-self.data['Close']
        self.data['CL'] = self.data['Close']-self.data['Low']
        self.data['True Range'] = \
        self.data[['HL','HC','CL']].max(axis=1).round(5)
        try:
            self.data['N'] = self.data['True Range'].rolling(20).mean().round(5)
            self.data['$Volatility'] = self.data['N']*self.data['Close']*100
        except:pass
        self.data['Account'] = self.balance
        try:
            self.data['Default Units'] = int(75000)
            self.data['Risk Adj Units'] = \
            self.data['Account']/self.data['$Volatility']
            self.data['Units'] = \
            self.data[['Default Units','Risk Adj Units']].mean(axis=1).astype(int)
            self.data['Average Units'] = self.data['Units'].rolling(20).mean()
            """
            if self.data.iloc[-1]['Units'] > 150000:
                self.data['Risk Adj Units'] = self.data['Default Units']
                self.data['Units'] = \
                self.data[['Default Units','Risk Adj Units']].max(axis=1).astype(int)
                self.data['Average Units'] = self.data['Units'].rolling(20).mean()
            if self.data['Units'].shape[0] > 60:
                self.data['Units'] = self.data['Average Units']
            """
            #self.data['Lot Size'] = \
            #self.data['Account']/self.data['$Volatility']
            #self.data['Lot Size'] = self.data['Lot Size'].fillna(0.0).astype(int)
        except:pass
        return self.data
    
    def minuteData(self):
        minuteData = self.data[['Open','High','Low','Close','20 High Close',
                                '50 High Close','20 Low Close','50 Low Close',
                                'True Range','N','Account','$Volatility',
                                'Units','Average Units']]
        return minuteData