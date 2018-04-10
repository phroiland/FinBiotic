#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:19:05 2017

@author: jonfroiland
"""

from resistance import Resistance
from support import Support


class Strategy(object):
    def __init__(self, instrument, dfD, mid, units, pivot,
                 rl1, rl2, rl3, sl1, sl2, sl3, rate1, rate2):
        # self.api = api
        # self._id = _id
        self.instrument = instrument
        self.dfD = dfD
        self.mid = mid
        # self.bid = float(bid)
        # self.ask = float(ask)
        self.units = units
        self.pivot = pivot
        self.rl1 = rl1
        self.rl2 = rl2
        self.rl3 = rl3
        self.sl1 = sl1
        self.sl2 = sl2
        self.sl3 = sl3
        self.rate1 = rate1
        self.rate2 = rate2

    def resistance_check(self):
        if self.mid > self.dfD.iloc[-1]['Daily Pivot Point']:
            # print '**** Checking Resistance Pivots ****'
            resistance = Resistance(
                self.instrument, self.dfD, self.mid, self.units, self.pivot,
                self.rl1, self.rl2, self.rl3, self.sl1, self.sl2, self.sl3, self.rate1, self.rate2
            )
            units, stop_loss, profit = resistance.resistance()
            return units, stop_loss, profit

    def support_check(self):
        if self.mid < self.dfD.iloc[-1]['Daily Pivot Point']:
            # print '**** Checking Support Pivots ****'
            support = Support(
                self.instrument, self.dfD, self.mid, self.units, self.pivot,
                self.rl1, self.rl2, self.rl3, self.sl1, self.sl2, self.sl3, self.rate1, self.rate2
            )
            units, stop_loss, profit = support.support()
            return units, stop_loss, profit
