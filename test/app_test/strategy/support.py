#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:53:58 2017

@author: jonfroiland
"""


class Support(object):

    def __init__(self, instrument, mid, dfD, units, pivot, sl1, sl2, sl3,
                 rate1, rate2):
        self.instrument = instrument
        self.mid = mid
        self.dfD = dfD
        self.units = units
        self.pivot = pivot
        self.sl1 = sl1
        self.sl2 = sl2
        self.sl3 = sl3
        self.rate1 = rate1
        self.rate2 = rate2

    def support(self):
        if (
                self.mid < self.pivot and self.mid > self.sl1 and
                self.units is not None and self.units > 0 and
                self.rate1 > .2 and self.rate1 < .4
                ):
            # print '*** Long PP_SL1 ***', self.units
            loss = self.sl1 - .00025
            return self.units, loss

        elif (
                self.mid < self.pivot and self.mid > self.sl1 and
                self.units is not None and self.units < 0 and
                self.rate2 > .2 and self.rate2 < .4
                ):
            # print '*** Short PP_SL1 ***', self.units
            loss = self.pivot + .00025
            return self.units, loss

        elif (
                self.mid < self.sl1 and self.mid > self.sl2 and
                self.units is not None and self.units > 0 and
                self.rate1 > .2 and self.rate1 < .4
                ):
            # print '*** Long SL1_SL2 ***', self.units
            loss = self.sl2 - .00025
            return self.units, loss

        elif (
                self.mid < self.sl1 and self.mid > self.sl2 and
                self.units is not None and self.units < 0 and
                self.rate2 > .2 and self.rate2 < .4
                ):
            # print '*** Short SL1_SL2 ***', self.units
            loss = self.sl1 + .00025
            return self.units, loss

        elif (
                self.mid < self.sl2 and self.mid > self.sl3 and
                self.units is not None and self.units > 0 and
                self.rate1 > .2 and self.rate1 < .4
                ):
            # print '*** Long SL1_SL2 ***', self.units
            loss = self.sl3 - .00025
            return self.units, loss

        elif (
                self.mid < self.sl2 and self.mid > self.sl3 and
                self.units is not None and self.units < 0 and
                self.rate2 > .2 and self.rate2 < .4
                ):
            # print '*** Short SL1_SL2 ***', self.units
            loss = self.sl2 + .00025
            return self.units, loss

        elif (
                self.mid < self.sl3 and self.units is not None and
                self.units > 0
                ):
            # print '*** Long SL3 Breakout ***', self.units
            loss = self.sl3
            return self.units, loss

        elif (
                self.mid < self.sl3 and self.units is not None and
                self.units < 0
                ):
            # print '*** Short RL3 Breakout ***', self.units
            loss = self.ask + .001
            return self.units, loss

        else:
            return None
