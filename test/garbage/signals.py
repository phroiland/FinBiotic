#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:34:25 2017

@author: jonfroiland
"""

class Breakout(object):
    def __init__(self, api, account_id, instrument, current, data):
        self.api = api
        self.account_id = account_id
        self.instrument = instrument
        self.current = current
        self.data = data
        
        self.PP_SL1 = self.PP_SL1()
        self.SL1_SL2 = self.SL1_SL2()
        self.SL2_RL3 = self.SL2_SL3()
    
    def breakout(self):
        if (
                self.data.shape[0]>20 and \
                self.data['High'][-1]>self.data['20 High Close'][-2] and \
                self.data['High'][-1] < \
                self.dfD.iloc[-1]['Daily Pivot Point'] and \
                self.data['High'][-1] > \
                self.dfD.iloc[-1]['Support Level 1']
            ):
            breakout = self.data['Lot Size'][-1] 
            print 'Long Breakout', breakout
            return breakout
        elif (
                self.data.shape[0]>20 and \
                self.data['Low'][-1]<self.data['20 Low Close'][-2] and \
                self.data['Low'][-1] > \
                self.dfD.iloc[-1]['Daily Pivot Point'] and \
                self.data['Low'][-1] < \
                self.dfD.iloc[-1]['Resistance Level 1']
            ):
            units = self.data['Lot Size'][-1]
            breakout = units*-1
            print 'Short Breakout', breakout
            return breakout
        else:pass
    
    def PP_SL1(self):
        if (
                self.current<self.dfD.iloc[-1]['Daily Pivot Point'] and \
                self.current>self.dfD.iloc[-1]['Support Level 1']
            ):
            over = self.current - self.dfD.iloc[-1]['Support Level 1']
            print over
            under = self.dfD.iloc[-1]['Daily Pivot Point'] - self.current
            print under
            try:
                spread = self.dfD.iloc[-1]['Daily Pivot Point'] - \
                        self.dfD.iloc[-1]['Support Level 1']
                print spread
                rate1 = over/spread
                print rate1
                rate2 = under/spread
                print rate2
                if rate1 > .13 and rate1 < .33:
                    PP_SL1 = self.data['Lot Size'][-1] 
                    print 'Long PP_SL1', PP_SL1
                    return PP_SL1
                if rate2 > .13 and rate2 < .33:
                    units = self.data['Lot Size'][-1]
                    PP_SL1 = units*-1
                    print 'Short PP_SL1', PP_SL1
                    return PP_SL1
            except:pass
    
    def SL1_SL2(self):
        if (
                self.current<self.dfD.iloc[-1]['Support Level 1'] and \
                self.current>self.dfD.iloc[-1]['Support Level 2']
            ):
            over = self.current - self.dfD.iloc[-1]['Support Level 2']
            print over
            under = self.dfD.iloc[-1]['Support Level 1'] - self.current
            print under
            try:
                spread = self.dfD.iloc[-1]['Support Level 1'] - \
                        self.dfD.iloc[-1]['Support Level 2']
                print spread
                rate1 = over/spread
                print rate1
                rate2 = under/spread
                print rate2
                if rate1 > .13 and rate1 < .33:
                    SL1_SL2 = self.data['Lot Size'][-1] 
                    print 'Long SL1_SL2', SL1_SL2
                    return SL1_SL2
                if rate2 > .13 and rate2 < .33:
                    units = self.data['Lot Size'][-1]
                    SL1_SL2 = units*-1
                    print 'Short SL1_SL2', SL1_SL2
                    return SL1_SL2
            except:pass
        
    def SL2_SL3(self):
        if (
                self.current<self.dfD.iloc[-1]['Support Level 2'] and \
                self.current>self.dfD.iloc[-1]['Support Level 3']
            ):
            over = self.current - self.dfD.iloc[-1]['Support Level 3']
            print over
            under = self.dfD.iloc[-1]['Support Level 2'] - self.current
            print under
            try:
                spread = self.dfD.iloc[-1]['Support Level 2'] - \
                        self.dfD.iloc[-1]['Support Level 3']
                print spread
                rate1 = over/spread
                print rate1
                rate2 = under/spread
                print rate2
                if rate1 > .13 and rate1 < .33:
                    SL2_SL3 = self.data['Lot Size'][-1] 
                    print 'Long SL2_SL3', SL2_SL3
                    return SL2_SL3
                if rate2 > .13 and rate2 < .33:
                    units = self.data['Lot Size'][-1]
                    SL2_SL3 = units*-1
                    print 'Short SL2_SL3', SL2_SL3
                    return SL2_SL3
            except:pass
        
    def sigArray(self):
        sigArray = []
        breakout = self.breakout
        pprl1 = self.PP_RL1
        rl1rl2 = self.RL1_RL2
        rl2rl3 = self.RL2_RL3
        ppsl1 = self.PP_SL1
        sl1sl2 = self.SL1_SL2
        sl2sl3 = self.SL2_RL3
        sigArray = [breakout,pprl1,rl1rl2,rl2rl3,ppsl1,sl1sl2,sl2sl3]
        for sigs in sigArray:
            if sigs is not None and sigs > 0 or sigs < 0:
                print 'SigArray',sigs
                return sigs
        
        
        
    