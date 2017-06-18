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
            'time': 8,
            'hour': 2,
            'type': 8,
            'price': 8,
            'volume': 8,
        }
        self.time_width = 8

    def print_time(self, candle):
        try:
            time = str(datetime.strptime(
                    candle.day, "%Y-%m-%dT%H:%M:%S.000000000Z").time())
        except:
            date = candle.time.split("T")[0]
            hour = candle.time.split("T")[1][0:5]
            time = date + ' ' + hour
        for price in ["mid", "bid", "ask"]:
            can = getattr(candle, price, None)

            if can is None:
                continue

            return "{:>{width[time]}}".format(
                time,
                width=self.width
            )

            time = ""

    def print_hour(self, candle):
        try:
            hour = str(datetime.strptime(
                    candle.day, "%Y-%m-%dT%H:%M:%S.000000000Z").time())
        except:
            hour = candle.time.split("T")[1][0:5]
            hour = int(hour[0:2])
        for price in ["mid", "bid", "ask"]:
            can = getattr(candle, price, None)

            if can is None:
                continue

            return "{:>{width[hour]}}".format(
                hour,
                width=self.width
            )

            hour = ""

    def print_open(self, candle):
        for price in ["mid", "bid", "ask"]:
            can = getattr(candle, price, None)

            if can is None:
                continue

            return "{:>{width[price]}}".format(
                can.o,
                width=self.width
            )

    def print_high(self, candle):
        for price in ["mid", "bid", "ask"]:
            can = getattr(candle, price, None)

            if can is None:
                continue

            return "{:>{width[price]}}".format(
                can.h,
                width=self.width
            )

    def print_low(self, candle):
        for price in ["mid", "bid", "ask"]:
            can = getattr(candle, price, None)

            if can is None:
                continue

            return "{:>{width[price]}}".format(
                can.l,
                width=self.width
            )

    def print_close(self, candle):
        for price in ["mid", "bid", "ask"]:
            can = getattr(candle, price, None)

            if can is None:
                continue

            return "{:>{width[price]}}".format(
                can.c,
                width=self.width
            )
