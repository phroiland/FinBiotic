#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:43:06 2017

@author: jonfroiland
"""

from datetime import datetime

class CandlePrinter(object):
    
    def __init__(self):
        self.width = {
            'time' : 8,
            'type' : 8,
            'price' : 8,
            'volume' : 8,
        }
        self.time_width = 8

    def print_time(self, candle):
        try:
            time = str(datetime.strptime(candle.day,"%Y-%m-%dT%H:%M:%S.000000000Z").time())
        except:
            time = candle.time.split("T")[0]

        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue
            
            return "{:>{width[time]}}".format(
                time,
                width=self.width
            )
            
            time = ""

    def print_open(self, candle):
        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue
            
            return "{:>{width[price]}}".format(
                c.o,
                width=self.width
            )
            
    def print_high(self, candle):
        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue
            
            return "{:>{width[price]}}".format(
                c.h,
                width=self.width
            )
            
    def print_low(self, candle):
        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue
            
            return "{:>{width[price]}}".format(
                c.l,
                width=self.width
            )
            
    def print_close(self, candle):
        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue
            
            return "{:>{width[price]}}".format(
                c.c,
                width=self.width
            )