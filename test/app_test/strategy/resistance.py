#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:31:27 2017

@author: jonfroiland
"""


class Resistance(object):

    def __init__(self, instrument, mid, dfD, units, pivot, rl1, rl2, rl3,
                 rate1, rate2):
        self.instrument = instrument
        self.mid = mid
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
                self.mid > self.pivot and self.mid < self.rl1 and
                self.units is not None and self.units > 0 and
                self.rate1 > .2 and self.rate1 < .4
                ):
            # print '*** Long PP_RL1 ***', self.units
            loss = self.pivot - .00025
            return self.units, loss

        elif (
                self.mid > self.pivot and self.mid < self.rl1 and
                self.units is not None and self.units < 0 and
                self.rate2 > .2 and self.rate2 < .4
                ):
            # print '*** Short PP_RL1 ***', self.units
            loss = self.rl1 + .00025
            return self.units, loss

        elif (
                self.mid > self.rl1 and self.mid < self.rl2 and
                self.units is not None and self.units > 0 and
                self.rate1 > .2 and self.rate1 < .4
                ):
            # print '*** Long RL1_RL2 ***', self.units
            loss = self.rl1 - .00025
            return self.units, loss

        elif (
                self.mid > self.rl1 and self.mid < self.rl2 and
                self.units is not None and self.units < 0 and
                self.rate2 > .2 and self.rate2 < .4
                ):
            # print '*** Short RL1_RL2 ***', self.units
            loss = self.rl2 + .00025
            return self.units, loss

        elif (
                self.mid > self.rl2 and self.mid < self.rl3 and
                self.units is not None and self.units > 0 and
                self.rate1 > .2 and self.rate1 < .4
                ):
            # print '*** Long RL2_RL3 ***', self.units
            loss = self.rl2 - .00025
            return self.units, loss

        elif (
                self.mid > self.rl2 and self.mid < self.rl3 and
                self.units is not None and self.units < 0 and
                self.rate2 > .2 and self.rate2 < .4
                ):
            # print '*** Short RL2_RL3 ***', self.units
            loss = self.rl3 + .00025
            return self.units, loss

        elif (
                self.mid > self.rl3 and self.units is not None and
                self.units > 0
                ):
            # print '*** Long RL3 Breakout ***', self.units
            loss = self.rl3
            return self.units, loss

        elif (
                self.mid > self.rl3 and self.units is not None and
                self.units < 0
                ):
            # print '*** Short RL3 Breakout ***', self.units
            loss = self.bid - .001
            return self.units, loss

        else:
            return None
