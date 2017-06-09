#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:19:05 2017

@author: jonfroiland
"""
from resistance import Resistance
from support import Support
from breakout import Breakout
from execute import Execute

class Strategy(object):
    
    def __init__(self, current, dfD, instrument, data, bid, ask, api, _id):
        self.current = float(current)
        self.dfD = dfD
        self.instrument = instrument
        self.data = data
        self.bid = float(bid)
        self.ask = float(ask)
        self.api = api
        self._id = _id
    
    def res_check(self):
        if self.current > self.dfD.iloc[-1]['Daily Pivot Point']:
            print '**** Checking Resistance Pivots ****'
            res = Resistance(self.instrument,self.current,self.dfD,self.data,
                             self.bid,self.ask)
            if res.resistance() is None:pass
            else:
                resUnits, resProfit, resLoss = res.resistance()
                resex = Execute(self.api,self._id,self.instrument,resUnits,
                                resProfit,resLoss)
                resex.trade()
    
    def sup_check(self):
        if self.current < self.dfD.iloc[-1]['Daily Pivot Point']:
            print '**** Checking Support Pivots ****'
            sup = Support(self.instrument,self.current,self.dfD,self.data,
                             self.bid,self.ask)
            if sup.support() is None:pass
            else:
                supUnits, supProfit, supLoss = sup.support()
                supex = Execute(self.api,self._id,self.instrument,supUnits,
                                supProfit,supLoss)
                supex.trade()
    
    def long_breakout(self):
        if self.current > self.dfD.iloc[-1]['Resistance Level 3']:
            print '**** Checking Breakout - Resistance ****'
            try:
                bo = Breakout(self.api,self._id,self.instrument,self.current,
                          self.data,self.dfD)
                if bo.res_breakout() is None:pass
            except Exception as e: print(e)
            else:
                try:
                    boUnits, boProfit, boLoss = \
                    bo.res_breakout()
                    boex = Execute(self.api,self._id,self.instrument,boUnits,
                                   boProfit,boLoss)
                    boex.trade()
                except Exception as e: print(e)
            return
        
    def short_breakout(self):
        if self.current < self.dfD.iloc[-1]['Support Level 3']:
            print '**** Checking Breakout - Support ****'
            try:
                bo = Breakout(self.api,self._id,self.instrument,self.current,
                          self.data,self.dfD)
                if bo.sup_breakout() is None:pass
            except Exception as e: print(e)
            else:
                try:
                    boUnits, boProfit, boLoss = \
                    bo.sup_breakout()
                    boex = Execute(self.api,self._id,self.instrument,boUnits,
                                   boProfit,boLoss)
                    boex.trade()
                except Exception as e: print(e)