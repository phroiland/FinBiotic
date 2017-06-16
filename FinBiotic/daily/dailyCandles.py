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
        
    def candleSet(self):
        df = pd.DataFrame([])
        df1 = pd.DataFrame({'Time':[self.printer.print_time(self.candle)]})
        df2 = pd.DataFrame({'Hour':[int(self.printer.print_hour(self.candle))]})
        df3 = pd.DataFrame({'Open':[float(self.printer.print_open(self.candle))]})
        df4 = pd.DataFrame({'High':[float(self.printer.print_high(self.candle))]})
        df5 = pd.DataFrame({'Low':[float(self.printer.print_low(self.candle))]})
        df6 = pd.DataFrame({'Close':[float(self.printer.print_close(self.candle))]})
        df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1, join='inner')
        return df