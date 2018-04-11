#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:30:38 2017

@author: jonfroiland
"""

import sys
import os
import settings
import argparse
import pandas as pd
import common.config
import common.args
from candlePrinter import CandlePrinter
from sessionCandles import Candles
from pivots import Pivots
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)


def main():
    candle_parser = argparse.ArgumentParser()

    common.config.add_argument(candle_parser)

    candle_parser.add_argument("instrument", type=common.args.instrument)

    candle_parser.add_argument("--mid", action='store_true',
                               help="Get midpoint-based candles")

    candle_parser.add_argument("--bid", action='store_true',
                               help="Get bid-based candles")

    candle_parser.add_argument("--ask", action='store_true',
                               help="Get ask-based candles")

    candle_parser.add_argument("--smooth", action='store_true',
                               help="'Smooth' the candles")

    # parser.set_defaults(mid=False, bid=False, ask=False)

    candle_parser.add_argument("--granularity", default='H1',
                               help="The candles granularity to fetch")

    candle_parser.add_argument("--from-time", default=None,
                               type=common.args.date_time(),
                               help="The start date for the candles to be \
                               fetched. Format is 'YYYY-MM-DD HH:MM:SS'")

    candle_parser.add_argument("--to-time", default=None,
                               type=common.args.date_time(),
                               help="The end date for the candles to be \
                               fetched. Format is 'YYYY-MM-DD HH:MM:SS'")

    candle_args = candle_parser.parse_args()
    candle_api = candle_args.config.create_context()

    kwargs = {}

    if candle_args.granularity is not None:
        kwargs["granularity"] = candle_args.granularity

    if candle_args.smooth is not None:
        kwargs["smooth"] = candle_args.smooth

    if candle_args.from_time is not None:
        kwargs["fromTime"] = candle_api.datetime_to_str(candle_args.from_time)

    if candle_args.to_time is not None:
        kwargs["toTime"] = candle_api.datetime_to_str(candle_args.to_time)

    candle_response = candle_api.instrument.candles(
        candle_args.instrument, **kwargs)

    if candle_response.status != 200:
        print(candle_response)
        print(candle_response.body)
        return

    print("Instrument: {}".format(candle_response.get("instrument", 200)))

    printer = CandlePrinter()

    globalDF = pd.DataFrame([])
    # tokyoDF = pd.DataFrame([])
    # minuteDF = pd.DataFrame([])
    for candle in candle_response.get("candles", 200):
        # tokyo = Candles(printer,candle).tokyoSession()
        # tokyoDF = tokyoDF.append(tokyo)
        _global = Candles(printer, candle).globalSession()
        globalDF = globalDF.append(_global)

    # tokyoDF = tokyoDF[['Time','Hour','Open','High','Low','Close']]
    # print tokyoDF.tail(), '\n'

    globalDF = globalDF[['Time', 'Hour', 'Open', 'High', 'Low', 'Close']]
    pair = sys.argv[1]
    globalDF.to_csv(os.path.join(settings.CSV_DIR, '%s_%s.csv' % (pair, 'Daily')), index=False)
    print(globalDF.tail())

    # Calculate Pivot Points, Resistance, and Support Lines
    Pivots(globalDF, pair)


if __name__ == "__main__":
    main()
