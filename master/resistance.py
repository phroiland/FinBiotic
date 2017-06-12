#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:31:27 2017

@author: jonfroiland
"""

class Resistance(object):
    
    def __init__(self, instrument, bid, ask, dfD, units, pivot, rl1, rl2, rl3,
                             rate1, rate2):
        self.instrument = instrument
        self.bid = bid
        self.ask = ask
        self.dfD = dfD
        self.units = units
        self.pivot = pivot
        self.rl1 = rl1
        self.rl2 = rl2
        self.rl3 = rl3
        self.rate1 = rate1
        self.rate2 = rate2

    def resistance(self):
        if (
                self.bid > self.pivot and self.ask < self.rl1 and \
                self.units is not None and self.units > 0 and \
                self.rate1 > .2 and self.rate1 < .4
            ):
            print '*** Long PP_RL1 ***', self.units
            profit = self.rl1
            loss = self.pivot
            return self.units, profit, loss
            
        elif (
                self.bid > self.pivot and self.ask < self.rl1 and \
                self.units is not None and self.units < 0 and \
                self.rate2 > .2 and self.rate2 < .4
            ):
            print '*** Short PP_RL1 ***', self.units
            profit = self.pivot
            loss = self.rl1
            return self.units, profit, loss
        
        elif (
                self.bid > self.rl1 and self.ask < self.rl2 and \
                self.units is not None and self.units > 0 and \
                self.rate1 > .2 and self.rate1 < .4
            ):
            print '*** Long RL1_RL2 ***', self.units
            profit = self.rl2
            loss = self.rl1
            return self.units, profit, loss
        
        elif (
                self.bid > self.rl1 and self.ask < self.rl2 and \
                self.units is not None and self.units < 0 and \
                self.rate2 > .2 and self.rate2 < .4
            ):
            print '*** Short RL1_RL2 ***', self.units
            profit = self.rl1
            loss = self.rl2
            return self.units, profit, loss 
        
        elif (
                self.bid > self.rl2 and self.ask < self.rl3 and \
                self.units is not None and self.units > 0 and \
                self.rate1 > .2 and self.rate1 < .4
            ):
            print '*** Long RL2_RL3 ***', self.units
            profit = self.rl3
            loss = self.rl2
            return self.units, profit, loss
        
        elif (
                self.bid > self.rl2 and self.ask < self.rl3 and \
                self.units is not None and self.units < 0 and \
                self.rate2 > .2 and self.rate2 < .4
            ):
            print '*** Short RL2_RL3 ***', self.units
            profit = self.rl2
            loss = self.rl3
            return self.units, profit, loss 
        
        elif (
                self.bid > self.rl3 and self.units is not None and \
                self.units > 0
            ):
            print '*** Long RL3 Breakout ***', self.units
            profit = self.ask + .002
            loss = self.rl3
            return self.units, profit, loss
        
        elif (
                self.bid > self.rl3 and self.units is not None and \
                self.units < 0
            ):
            print '*** Short RL3 Breakout ***', self.units
            profit = self.rl3
            loss = self.bid - .001
            return self.units, profit, loss
        
        else:
            return None