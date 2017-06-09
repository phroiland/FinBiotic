#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:34:25 2017

@author: jonfroiland
"""

class Breakout(object):
    def __init__(self, api, account_id, instrument, current, data, dfD):
        self.api = api
        self.account_id = account_id
        self.instrument = instrument
        self.current = float(current)
        self.data = data
        self.dfD = dfD
       
    def res_breakout(self):
        if (
                self.data.shape[0]>20 and \
                self.data['High'][-1]>self.data['20 High Close'][-2] and \
                self.data['High'][-1] > \
                self.dfD.iloc[-1]['Resistance Level 3']
            ):
            units = self.data['Lot Size'][-1].astype(int) 
            print 'Long Breakout', units
            profit = 5*self.data.iloc[-1]['N'].round(5) + self.current
            loss = self.dfD.iloc[-1]['Resistance Level 3']
            return units, profit, loss
        else:return None
    
    def sup_breakout(self):
        if (
                self.data.shape[0]>20 and \
                self.data['Low'][-1]<self.data['20 Low Close'][-2] and \
                self.data['Low'][-1] < \
                self.dfD.iloc[-1]['Support Level 3']
            ):
            units = self.data['Lot Size'][-1].astype(int)
            units = units*-1
            print 'Short Breakout', units
            profit = -5*self.data.iloc[-1]['N'].round(5) + self.current
            loss = self.dfD.iloc[-1]['Support Level 3']
            return units, profit, loss
        else:return None