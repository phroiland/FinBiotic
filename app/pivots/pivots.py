#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:57:23 2017

@author: jonfroiland
"""
import settings
import os
import os.path
import pandas as pd
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)


class Pivots(object):

    def __init__(self, df, pair):
        self.df = df
        self.pair = pair
        self.dailyPP = self.daily_pivot_point()
        self.rl1D = self.RL_1D()
        self.sl1D = self.SL_1D()
        self.rl2D = self.RL_2D()
        self.sl2D = self.SL_2D()
        self.rl3D = self.RL_3D()
        self.sl3D = self.SL_3D()
        self.weeklyPP = self.weekly_pivot_point()
        self.rl1W = self.RL_1W()
        self.sl1W = self.SL_1W()
        self.rl2W = self.RL_2W()
        self.sl2W = self.SL_2W()
        self.rl3W = self.RL_3W()
        self.sl3W = self.SL_3W()
        self.dailyPPRS = self.dailyPivotsDF()
        self.weeklyPPRS = self.weeklyPivotsDF()

    def daily_pivot_point(self):
        dailyHigh = self.df.iloc[-2]['High']
        dailyLow = self.df.iloc[-2]['Low']
        dailyClose = self.df.iloc[-2]['Close']
        dailyPP = (dailyHigh+dailyLow+dailyClose)/3
        return dailyPP

    def RL_1D(self):
        RL_1D = (2*self.dailyPP) - self.df.iloc[-2]['Low']
        return RL_1D

    def SL_1D(self):
        SL_1D = (2*self.dailyPP) - self.df.iloc[-2]['High']
        return SL_1D

    def RL_2D(self):
        RL_2D = (self.dailyPP - self.sl1D) + self.rl1D
        return RL_2D

    def SL_2D(self):
        SL_2D = self.dailyPP - (self.rl1D-self.sl1D)
        return SL_2D

    def RL_3D(self):
        RL_3D = (self.dailyPP-self.sl2D) + self.rl2D
        return RL_3D

    def SL_3D(self):
        SL_3D = self.dailyPP - (self.rl2D-self.sl2D)
        return SL_3D

    def weekly_pivot_point(self):
        weeklyHigh = self.df.iloc[-6:-2]['High'].max()
        weeklyLow = self.df.iloc[-6:-2]['Low'].min()
        weeklyClose = self.df.iloc[-2]['Close']
        weeklyPP = (weeklyHigh+weeklyLow+weeklyClose)/3
        return weeklyPP

    def RL_1W(self):
        RL_1W = (2*self.weeklyPP) - self.df.iloc[-6:-2]['Low'].min()
        return RL_1W

    def SL_1W(self):
        SL_1W = (2*self.weeklyPP) - self.df.iloc[-6:-2]['High'].max()
        return SL_1W

    def RL_2W(self):
        RL_2W = (self.weeklyPP - self.sl1W) + self.rl1W
        return RL_2W

    def SL_2W(self):
        SL_2W = self.weeklyPP - (self.rl1W-self.sl1W)
        return SL_2W

    def RL_3W(self):
        RL_3W = (self.weeklyPP-self.sl2W) + self.rl2W
        return RL_3W

    def SL_3W(self):
        SL_3W = self.weeklyPP - (self.rl2W-self.sl2W)
        return SL_3W

    def dailyPivotsDF(self):
        # time = self.df.iloc[-2]['Time']
        dailyPPRS = pd.DataFrame([])
        dfD = pd.DataFrame({'Daily Pivot Point': [self.dailyPP]})
        dfRL1D = pd.DataFrame({'Resistance Level 1': [self.rl1D]})
        dfSL1D = pd.DataFrame({'Support Level 1': [self.sl1D]})
        dfRL2D = pd.DataFrame({'Resistance Level 2': [self.rl2D]})
        dfSL2D = pd.DataFrame({'Support Level 2': [self.sl2D]})
        dfRL3D = pd.DataFrame({'Resistance Level 3': [self.rl3D]})
        dfSL3D = pd.DataFrame({'Support Level 3': [self.sl3D]})

        pprs_out = pd.concat([dfD, dfRL1D, dfSL1D, dfRL2D, dfSL2D, dfRL3D,
                              dfSL3D], axis=1, join='inner')
        dailyPPRS = dailyPPRS.append(pprs_out)
        dailyPPRS.to_csv(os.path.join(
                settings.CSV_DIR, "%s_%s.csv" % (
                        self.pair, 'DailyPivots')), index=False)
        # print dailyPPRS
        return dailyPPRS

    def weeklyPivotsDF(self):
        # time = self.df.iloc[-2]['Time']
        weeklyPPRS = pd.DataFrame([])
        dfD = pd.DataFrame({'Weekly Pivot Point': [self.weeklyPP]})
        dfRL1D = pd.DataFrame({'Resistance Level 1': [self.rl1W]})
        dfSL1D = pd.DataFrame({'Support Level 1': [self.sl1W]})
        dfRL2D = pd.DataFrame({'Resistance Level 2': [self.rl2W]})
        dfSL2D = pd.DataFrame({'Support Level 2': [self.sl2W]})
        dfRL3D = pd.DataFrame({'Resistance Level 3': [self.rl3W]})
        dfSL3D = pd.DataFrame({'Support Level 3': [self.sl3W]})

        pprs_out = pd.concat([dfD, dfRL1D, dfSL1D, dfRL2D, dfSL2D, dfRL3D,
                              dfSL3D], axis=1, join='inner')
        weeklyPPRS = weeklyPPRS.append(pprs_out)
        weeklyPPRS.to_csv(os.path.join(
                settings.CSV_DIR, "%s_%s.csv" % (
                        self.pair, 'WeeklyPivots')), index=False)
        # print weeklyPPRS
        return weeklyPPRS
