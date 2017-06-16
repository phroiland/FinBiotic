#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:12:26 2017

@author: jonfroiland
"""
import pandas as pd

class Tokyo(object):
    
    def __init__(self, df, pair):
        self.df = df
        self.pair = pair
    
    def tokyoDF(self):
        if self.df['Hour'] == 0 and self.df['Hour'] < 7:
            tokyoDF = pd.DataFrame([])
            tokyoDF = tokyoDF.append(self.df)
            
        
