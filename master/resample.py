#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 00:32:21 2017

@author: jonfroiland
"""
import pandas as pd

class Resample(object):
    
    def __init__(self, df, balance):
        self.df = df
        self.balance = balance
        self.data = self.resample()
        
    def resample(self):
        xx = self.df.to_period(freq=self.xsec)
        openCol = xx.resample(self.xmin).first()
        highCol = xx.resample(self.xmin).max()
        lowCol = xx.resample(self.xmin).min()
        closeCol = xx.resample(self.xmin).last()
        data = pd.concat([openCol,highCol,lowCol,closeCol],
                               axis=1,join='inner')
        data['Open'] = openCol.round(5)
        data['High'] = highCol.round(5)
        data['Low'] = lowCol.round(5)
        data['Close'] = closeCol.round(5)
        try:
            data['Open'] = data['Open'].fillna(method='ffill')
            data['High'] = data['High'].fillna(method='ffill')
            data['Low'] = data['Low'].fillna(method='ffill')
            data['Close'] = data['Close'].fillna(method='ffill')
        except:pass
        data['20 High Close'] = data['Close'].rolling(20).max()
        data['20 Low Close'] = data['Close'].rolling(20).min()
        data['50 High Close'] = data['Close'].rolling(50).max()
        data['50 Low Close'] = data['Close'].rolling(50).min()
        data['HL'] = data['High']-data['Low']
        data['HC'] = data['High']-data['Close']
        data['CL'] = data['Close']-data['Low']
        data['True Range'] = \
        data[['HL','HC','CL']].max(axis=1).round(5)
        try:
            data['N'] = data['True Range'].rolling(20).mean().round(5)
            data['$Volatility'] = data['N']*data['Close']*100
        except:pass
        data['Account'] = self.balance
        try:
            data['Default Units'] = int(50000)
            data['Risk Adj Units'] = \
            data['Account']/data['$Volatility']
            data['Units'] = \
            data[['Default Units','Risk Adj Units']].mean(axis=1).astype(int)
            data['Average Units'] = data['Units'].rolling(20).mean()
        except:pass
        return data
    
    def minuteData(self):
        minuteData = self.data[['Open','High','Low','Close','20 High Close',
                  '20 Low Close','True Range','N','Account','$Volatility',
                  'Units','Average Units']]
        return minuteData