#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:48:11 2017

@author: jonfroiland
"""
import argparse
import common.config
import common.args
from candlePrinter import CandlePrinter
import pandas as pd
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)


parser = argparse.ArgumentParser()
common.config.add_argument(parser)

class Candles(object):
    
    def __init__(self,instrument):
        self.instrument = instrument
        self.args = self.candleSet()
        self.api = self.candleSet()
        self.response = self.candleSet()
        
    def candleSet(self):
    
        parser.add_argument("instrument",type=common.args.instrument)
        parser.add_argument("--mid",action='store_true')
        parser.add_argument("--bid",action='store_true')
        parser.add_argument("--ask",action='store_true')
        parser.add_argument("--smooth",action='store_true')
        parser.set_defaults(mid=False, bid=False, ask=False)
        parser.add_argument("--granularity",default='D')
        parser.add_argument("--from-time",default='2017-05-27 00:00:00',
                            type=common.args.date_time())
    
        parser.add_argument("--to-time",default='2017-06-05 22:30:00',
                            type=common.args.date_time())
    
        args = parser.parse_args()
        api = args.config.create_context()
    
        kwargs = {}
    
        if args.granularity is not None:
            kwargs["granularity"] = args.granularity
    
        if args.smooth is not None:
            kwargs["smooth"] = args.smooth
            
        if args.from_time is not None:
            kwargs["fromTime"] = api.datetime_to_str(args.from_time)
    
        if args.to_time is not None:
            kwargs["toTime"] = api.datetime_to_str(args.to_time)
    
        response = api.instrument.candles(args.instrument, **kwargs)
        
        print("Instrument: {}".format(response.get("instrument", 200)))
        
        if response.status != 200:
            print(response)
            print(response.body)
            return
        
        else:
            return args, api, response
    
    def candlePrinter(self):
        printer = CandlePrinter()

        df = pd.DataFrame([])
        df_out = pd.DataFrame([])
        
        for candle in self.response.get("candles", 200):
            
            df1 = pd.DataFrame({'Time':[printer.print_time(candle)]})
            df2 = pd.DataFrame({'Open':[float(printer.print_open(candle))]})
            df3 = pd.DataFrame({'High':[float(printer.print_high(candle))]})
            df4 = pd.DataFrame({'Low':[float(printer.print_low(candle))]})
            df5 = pd.DataFrame({'Close':[float(printer.print_close(candle))]})
            
            df_out = pd.concat([df1, df2, df3, df4, df5], axis=1, join='inner')
            df = df.append(df_out)
        df = df.dropna()
        candlesDF = df[['Time','Open','High','Low','Close']]
        return candlesDF