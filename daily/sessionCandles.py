#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:48:11 2017

@author: jonfroiland
"""
import pandas as pd


class Candles(object):

    def __init__(self, printer, candle):
        self.printer = printer
        self.candle = candle
        self.time = pd.DataFrame({'Time': [
                self.printer.print_time(self.candle)]})
        self.hour = pd.DataFrame({'Hour': [
                int(self.printer.print_hour(self.candle))]})
        self.open = pd.DataFrame({'Open': [
                float(self.printer.print_open(self.candle))]})
        self.high = pd.DataFrame({'High': [
                float(self.printer.print_high(self.candle))]})
        self.low = pd.DataFrame({'Low': [
                float(self.printer.print_low(self.candle))]})
        self.close = pd.DataFrame({'Close': [
                float(self.printer.print_low(self.candle))]})

    def tokyoSession(self):
        if (
                int(self.printer.print_hour(self.candle)) >= 0 and
                int(self.printer.print_hour(self.candle)) < 8
                ):
                df1 = self.time
                df2 = self.hour
                df3 = self.open
                df4 = self.high
                df5 = self.low
                df6 = self.close
                df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1,
                               join='inner')
                return df

    def londonSession(self):
        if (
                int(self.printer.print_hour(self.candle)) >= 7 and
                int(self.printer.print_hour(self.candle)) >= 17
                ):
                df1 = self.time
                df2 = self.hour
                df3 = self.open
                df4 = self.high
                df5 = self.low
                df6 = self.close
                df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1,
                               join='inner')
                return df

    def nySession(self):
        if (
                int(self.printer.print_hour(self.candle)) >= 12 and
                int(self.printer.print_hour(self.candle)) < 22
                ):
                df1 = self.time
                df2 = self.hour
                df3 = self.open
                df4 = self.high
                df5 = self.low
                df6 = self.close
                df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1,
                               join='inner')
                return df

    def globalSession(self):
        if int(self.printer.print_hour(self.candle)) >= 0:
                df1 = self.time
                df2 = self.hour
                df3 = self.open
                df4 = self.high
                df5 = self.low
                df6 = self.close
                df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1,
                               join='inner')
                return df
