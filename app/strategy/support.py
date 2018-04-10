#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:53:58 2017

@author: jonfroiland
"""


class Support(object):

    def __init__(self, instrument, dfD, mid, units, pivot, rl1, rl2, rl3, sl1, sl2, sl3, rate1, rate2):
        self.instrument = instrument
        self.dfD = dfD
        self.mid = float(mid)
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

    def support(self):
        if (
                self.pivot > self.mid > self.sl1 and
                self.units is not None and self.units > 0 and
                .236 < self.rate1 < .382
                ):
            # print '*** Long PP_SL1 ***', self.units
            stop_loss = self.sl2
            profit = self.pivot
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.pivot > self.mid > self.sl1 and
                self.units is not None and self.units < 0 and
                .236 < self.rate2 < .382
                ):
            # print '*** Short PP_SL1 ***', self.units
            stop_loss = self.rl1
            profit = self.sl1
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.sl1 > self.mid > self.sl2 and
                self.units is not None and self.units > 0 and
                .236 < self.rate1 < .382
                ):
            # print '*** Long SL1_SL2 ***', self.units
            stop_loss = self.sl3
            profit = self.sl1
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.sl1 > self.mid > self.sl2 and
                self.units is not None and self.units < 0 and
                .236 < self.rate2 < .382
                ):
            # print '*** Short SL1_SL2 ***', self.units
            stop_loss = self.pivot
            profit = self.sl2
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.sl2 > self.mid > self.sl3 and
                self.units is not None and self.units > 0 and
                .236 < self.rate1 < .382
                ):
            # print '*** Long SL2_SL3 ***', self.units
            stop_loss = self.sl3 - .00025
            profit = self.sl2
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.sl2 > self.mid > self.sl3 and
                self.units is not None and self.units < 0 and
                .236 < self.rate2 < .382
                ):
            # print '*** Short SL2_SL3 ***', self.units
            stop_loss = self.sl1
            profit = self.sl3
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.mid < self.sl3 and self.units is not None and
                self.units > 0
                ):
            # print '*** Long SL3 Breakout ***', self.units
            stop_loss = self.sl3 - .00025
            profit = self.sl3 + .001
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.mid < self.sl3 and self.units is not None and
                self.units < 0
                ):
            # print '*** Short SL3 Breakout ***', self.units
            stop_loss = self.sl2
            profit = self.sl3 - .001
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        else:
            # print 'Support held, no trades executed'
            return None
