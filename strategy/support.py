#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:53:58 2017

@author: jonfroiland
"""
class Support(object):
    
    def __init__(self, instrument, current, dfD, units, bid, ask):
        self.instrument = instrument
        self.current = float(current)
        self.dfD = dfD
        self.units = units
        self.bid = float(bid)
        self.ask = float(ask)
        
    def support(self):
        if (
                self.current<self.dfD.iloc[-1]['Daily Pivot Point'].round(5) and \
                self.current>self.dfD.iloc[-1]['Support Level 1']
            ):
            over = self.current - self.dfD.iloc[-1]['Support Level 1']
            under = self.dfD.iloc[-1]['Daily Pivot Point'] - self.current
            spread = self.dfD.iloc[-1]['Daily Pivot Point'] - \
                    self.dfD.iloc[-1]['Support Level 1']
            rate1 = over/spread
            rate2 = under/spread
            entryLow = self.units.iloc[-1]['N']/spread
            entryHigh = (2*self.units.iloc[-1]['N'])/spread
            if rate1 > entryLow and rate1 < entryHigh:
                units = self.units.iloc[-1]['Lot Size'].astype(int)
                loss = self.dfD.iloc[-1]['Support Level 1'] \
                + self.units.iloc[-1]['N']
                loss = loss.round(5)
                profit = self.dfD.iloc[-1]['Daily Pivot Point'] \
                - self.units.iloc[-1]['N']
                profit = profit.round(5)
                print 'Long PP_SL1', units
                return units, profit, loss
            elif rate2 > entryLow and rate2 < entryHigh:
                units = self.units.iloc[-1]['Lot Size'].astype(int)
                units = units*-1
                profit = self.dfD.iloc[-1]['Support Level 1'] \
                + self.units.iloc[-1]['N']
                profit = profit.round(5)
                loss = self.dfD.iloc[-1]['Daily Pivot Point'] \
                - self.units.iloc[-1]['N']
                loss = loss.round(5)
                print 'Short PP_SL1', units
                return units, profit, loss
        elif (
                self.current<self.dfD.iloc[-1]['Support Level 1'] and \
                self.current>self.dfD.iloc[-1]['Support Level 2']
            ):
            over = self.current - self.dfD.iloc[-1]['Support Level 2']
            under = self.dfD.iloc[-1]['Support Level 1'] - self.current
            spread = self.dfD.iloc[-1]['Support Level 1'] - \
                    self.dfD.iloc[-1]['Support Level 2']
            rate1 = over/spread
            rate2 = under/spread
            entryLow = self.units.iloc[-1]['N']/spread
            entryHigh = (2*self.units.iloc[-1]['N'])/spread
            if rate1 > entryLow and rate1 < entryHigh:
                units = self.units.iloc[-1]['Lot Size'].astype(int)
                loss = self.dfD.iloc[-1]['Support Level 2'] \
                + self.units.iloc[-1]['N']
                loss = loss.round(5)
                profit = self.dfD.iloc[-1]['Support Level 1'] \
                - self.units.iloc[-1]['N']
                profit = profit.round(5)
                print 'Long SL1_SL2', units
                return units, profit, loss
            elif rate2 > entryLow and rate2 < entryHigh:
                units = self.units.iloc[-1]['Lot Size'].astype(int)
                units = units*-1
                profit = self.dfD.iloc[-1]['Support Level 2'] \
                + self.units.iloc[-1]['N']
                profit = profit.round(5)
                loss = self.dfD.iloc[-1]['Support Level 1'] \
                - self.units.iloc[-1]['N']
                loss = loss.round(5)
                print 'Short SL1_SL2', units
                return units, profit, loss
        elif (
                self.current<self.dfD.iloc[-1]['Support Level 2'] and \
                self.current>self.dfD.iloc[-1]['Support Level 3']
            ):
            over = self.current - self.dfD.iloc[-1]['Support Level 3']
            under = self.dfD.iloc[-1]['Support Level 2'] - self.current
            spread = self.dfD.iloc[-1]['Support Level 2'] - \
                    self.dfD.iloc[-1]['Support Level 3']
            rate1 = over/spread
            rate2 = under/spread
            entryLow = self.units.iloc[-1]['N']/spread
            entryHigh = (2*self.units.iloc[-1]['N'])/spread
            if rate1 > entryLow and rate1 < entryHigh:
                units = self.units.iloc[-1]['Lot Size'].astype(int)
                loss = self.dfD.iloc[-1]['Support Level 3'] \
                + self.units.iloc[-1]['N']
                loss = loss.round(5)
                profit = self.dfD.iloc[-1]['Support Level 2'] \
                - self.units.iloc[-1]['N']
                profit = profit.round(5)
                print 'Long SL2_SL3', units
                return units, profit, loss
            elif rate2 > entryLow and rate2 < entryHigh:
                units = self.units.iloc[-1]['Lot Size'].astype(int)
                profit = self.dfD.iloc[-1]['Support Level 3'] \
                + self.units.iloc[-1]['N']
                profit = profit.round(5)
                loss = self.dfD.iloc[-1]['Support Level 2'] \
                - self.units.iloc[-1]['N']
                loss = loss.round(5)
                units = units*-1
                print 'Short SL2_SL3', units
                return units, profit, loss
        else:
            return None