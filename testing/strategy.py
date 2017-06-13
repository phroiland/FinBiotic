#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:19:05 2017

@author: jonfroiland
"""
from resistance import Resistance
from support import Support
from execute import Execute

class Strategy(object):
    
    def __init__(self, api, _id, instrument, dfD, mid, breakout, pivot, 
                 rl1, rl2, rl3, sl1, sl2, sl3, rate1, rate2):
        self.api = api
        self._id = _id
        self.instrument = instrument
        self.dfD = dfD
        self.mid = float(mid)
        #self.bid = float(bid)
        #self.ask = float(ask)
        self.units = breakout
        self.pivot = pivot
        self.rl1 = rl1
        self.rl2 = rl2
        self.rl3 = rl3
        self.sl1 = sl1
        self.sl2 = sl2
        self.sl3 = sl3
        self.rate1 = rate1
        self.rate2 = rate2
        
    def res_check(self):
        if self.mid > self.dfD.iloc[-1]['Daily Pivot Point']:
            print '**** Checking Resistance Pivots ****'
            res = Resistance(self.instrument,self.mid,self.dfD,
                             self.units,self.pivot,self.rl1,self.rl2,self.rl3,
                             self.rate1,self.rate2)
            print res.resistance()
            try:
                resUnits, resProfit, resLoss = res.resistance()
                resex = Execute(self.api,self._id,self.instrument,resUnits,
                                resProfit,resLoss)
                resex.trade()
            except Exception as e: print(e)
    def sup_check(self):
        if self.mid < self.dfD.iloc[-1]['Daily Pivot Point']:
            print '**** Checking Support Pivots ****'
            sup = Support(self.instrument,self.mid,self.dfD,
                          self.units,self.pivot,self.sl1,self.sl2,self.sl3,
                             self.rate1,self.rate2)
            print sup.support()
            try:
                supUnits, supProfit, supLoss = sup.support()
                supex = Execute(self.api,self._id,self.instrument,supUnits,
                                supProfit,supLoss)
                supex.trade()
            except Exception as e: print(e)