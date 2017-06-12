#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:12:26 2017

@author: jonfroiland
"""

class Spreads(object):
    
    def __init__(self, dfD, bid, ask):
        self.dfD = dfD
        self.bid = bid
        self.ask = ask
        self.pivot = self.spreads()
        self.rl1 = self.spreads()
        self.rl2 = self.spreads()
        self.rl3 = self.spreads()
        self.sl1 = self.spreads()
        self.sl2 = self.spreads()
        self.sl3 = self.spreads()
        
    def spreads(self):
        pivot = self.dfD.iloc[-1]['Daily Pivot Point'].round(5)
        rl1 = self.dfD.iloc[-1]['Resistance Level 1'].round(5)
        rl2 = self.dfD.iloc[-1]['Resistance Level 2'].round(5)
        rl3 = self.dfD.iloc[-1]['Resistance Level 3'].round(5)
        sl1 = self.dfD.iloc[-1]['Support Level 1'].round(5)
        sl2 = self.dfD.iloc[-1]['Support Level 2'].round(5)
        sl3 = self.dfD.iloc[-1]['Support Level 3'].round(5)
        return pivot, rl1, rl2, rl3, sl1, sl2, sl3
        
    def spreads_out(self):
        if self.bid > self.pivot and self.ask < self.rl1:
            over = self.bid - self.pivot
            spread = self.rl1 - self.pivot
            rate1 = over/spread
            rate2 = 1 - rate1
            print "PP_RL1", over, spread, rate1, rate2
            return rate1, rate2
        
        elif self.bid > self.rl1 and self.ask < self.rl2:
            over = self.bid - self.rl1
            spread = self.rl2 - self.rl1
            rate1 = over/spread
            rate2 = 1 - rate1
            print "RL1_RL2", over, spread, rate1, rate2
            return rate1, rate2
        
        elif self.bid > self.rl2 and self.ask < self.rl3:
            over = self.bid - self.rl2
            spread = self.rl3 - self.rl2
            rate1 = over/spread
            rate2 = 1 - rate1
            print "RL2_RL3", over, spread, rate1, rate2
            return rate1, rate2
        
        elif self.ask < self.pivot and self.bid > self.sl1:
            over = self.ask - self.sl1
            spread = self.pivot - self.sl1
            rate1 = over/spread
            rate2 = 1 - rate1
            print "PP_SL1", over, spread, rate1, rate2
            return rate1, rate2
        
        elif self.ask < self.sl1 and self.bid > self.sl2:
            over = self.ask - self.sl2
            spread = self.sl1 - self.sl2
            rate1 = over/spread
            rate2 = 1 - rate1
            print "SL1_SL2", over, spread, rate1, rate2
            return rate1, rate2
        
        elif self.ask < self.sl2 and self.bid > self.sl3:
            over = self.ask - self.sl3
            spread = self.sl2 - self.sl3
            rate1 = over/spread
            rate2 = 1 - rate1
            print "SL2_SL3", over, spread, rate1, rate2
            return rate1, rate2
        
        else:pass