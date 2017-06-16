#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:32:50 2017

@author: jonfroiland
"""
import pandas as pd
import os, os.path
import settings

class PivotImports(object):
    def __init__(self, instrument, date):
        self.instrument = instrument
        self.date = date
        
    def daily(self):
        dfD = pd.read_csv(os.path.join(settings.CSV_DIR,"%s_%s.csv" % (
            self.instrument,'DailyPivots')))
        print dfD
        return dfD

    def weekly(self):
        dfW = pd.read_csv(os.path.join(settings.CSV_DIR,"%s_%s.csv" % (
                self.instrument,'WeeklyPivots')))
        print dfW
        return dfW