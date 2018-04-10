#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:31:27 2017

@author: jonfroiland
"""


class Resistance(object):

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

    def resistance(self):
        if (
                self.pivot < self.mid < self.rl1 and
                self.units is not None and self.units > 0 and
                .236 < self.rate1 < .382
                ):
            # print '*** Long PP_RL1 ***', self.units
            stop_loss = self.sl1
            profit = self.rl1
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.pivot < self.mid < self.rl1 and
                self.units is not None and self.units < 0 and
                .236 < self.rate2 < .382
                ):
            # print '*** Short PP_RL1 ***', self.units
            stop_loss = self.rl2
            profit = self.pivot
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.rl1 < self.mid < self.rl2 and
                self.units is not None and self.units > 0 and
                .236 < self.rate1 < .382
                ):
            # print '*** Long RL1_RL2 ***', self.units
            stop_loss = self.pivot
            profit = self.rl2
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.rl1 < self.mid < self.rl2 and
                self.units is not None and self.units < 0 and
                .236 < self.rate2 < .382
                ):
            # print '*** Short RL1_RL2 ***', self.units
            stop_loss = self.rl3
            profit = self.rl1
            # rint 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.rl2 < self.mid < self.rl3 and
                self.units is not None and self.units > 0 and
                .236 < self.rate1 < .382
                ):
            # print '*** Long RL2_RL3 ***', self.units
            stop_loss = self.rl1
            profit = self.rl3
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.rl2 < self.mid < self.rl3 and
                self.units is not None and self.units < 0 and
                .236 < self.rate2 < .382
                ):
            # print '*** Short RL2_RL3 ***', self.units
            stop_loss = self.rl3 + .00025
            profit = self.rl2
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.mid > self.rl3 and self.units is not None and
                self.units > 0
                ):
            # print '*** Long RL3 Breakout ***', self.units
            stop_loss = self.rl2
            profit = self.rl3 + .001
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        elif (
                self.mid > self.rl3 and self.units is not None and
                self.units < 0
                ):
            # print '*** Short RL3 Breakout ***', self.units
            stop_loss = self.rl3 - .00025
            profit = self.rl2
            # print 'Stop Loss', stop_loss
            # print 'Profit', profit
            return self.units, stop_loss, profit

        else:
            # print 'Resistance held, no trades executed'
            return None
