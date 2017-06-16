#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:34:25 2017

@author: jonfroiland
"""
class Breakout(object):
    def __init__(self, data, mid):
        self.data = data
        self.mid = float(mid)
        
    def breakout(self):
        
        if (
                self.mid > self.data.iloc[-1]['Low'] and \
                self.data.shape[0] > 50 and \
                self.data.iloc[-1]['High'] > \
                self.data.iloc[-2]['20 High Close'] and \
                self.data.iloc[-1]['High'] > \
                self.data.iloc[-2]['50 High Close']
            ):
            print '*** Long 20/50 Breakout ***'
            units = self.data.iloc[-1]['Units'].astype(int)
            print units
            return units
        
        elif (
                self.mid < self.data.iloc[-1]['High'] and \
                self.data.shape[0] > 50 and \
                self.data.iloc[-1]['Low'] < \
                self.data.iloc[-2]['20 Low Close'] and \
                self.data.iloc[-1]['Low'] < \
                self.data.iloc[-2]['50 Low Close']
            ):
            print '*** Short 20/50 Breakout ***'
            units = self.data.iloc[-1]['Units'].astype(int)
            units = units*-1
            print units
            return units
        
        elif (
                self.mid > self.data.iloc[-1]['Low'] and \
                self.data.shape[0] > 20 and \
                self.data.iloc[-1]['High'] > \
                self.data.iloc[-2]['20 High Close']
            ):
            print '*** Long 20 Breakout ***'
            units = self.data.iloc[-1]['Units'].astype(int)
            print units
            return units
        
        elif (
                self.mid < self.data.iloc[-1]['High'] and \
                self.data.shape[0] > 20 and \
                self.data.iloc[-1]['Low'] < \
                self.data.iloc[-2]['20 Low Close']
            ):
            print '*** Short 20 Breakout ***'
            units = self.data.iloc[-1]['Units'].astype(int)
            units = units*-1
            print units
            return units
        
        else:return None