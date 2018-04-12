#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:30:38 2017

@author: jonfroiland
"""

import sys
import argparse

import oandapyV20
import oandapyV20.endpoints.positions as openPos

# Data, Price, and Strategy Imports
import settings
import common.config
import common.args
from execute.execute import Execute
from stream.streamingData import StreamingData
from stream.view import mid_string, heartbeat_to_string, instrument_string
from account.balance import Balance
from strategy.breakout import Breakout
from strategy.spreads import Spreads
from strategy.strategy import Strategy
from pivots.pivotImports import PivotImports

# from view import bid_string, ask_string, price_to_string
from datetime import datetime
import pandas as pd

pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)


def main():
    print "------ System online -------", datetime.now()

    parser = argparse.ArgumentParser()

    common.config.add_argument(parser)

    parser.add_argument('--instrument', "-i", type=common.args.instrument,
                        required=True, action="append",
                        help="Instrument to get prices for")

    parser.add_argument('--snapshot', action="store_true", default=True,
                        help="Request an initial snapshot")

    parser.add_argument('--no-snapshot', dest="snapshot", action="store_false",
                        help="Do not request an initial snapshot")

    parser.add_argument('--show-heartbeats', "-s", action='store_true',
                        default=False, help="display heartbeats")

    args = parser.parse_args()
    account_id = args.config.active_account
    api = args.config.create_streaming_context()
    account_api = args.config.create_context()

    response = api.pricing.stream(account_id, snapshot=args.snapshot,
                                  instruments=",".join(args.instrument))

    dfD = PivotImports(sys.argv[2]).daily()
    # dfW = p.weekly()
    balance = Balance(account_api, account_id).balance()

    df = pd.DataFrame([])

    for msg_type, msg in response.parts():
        if msg_type == 'pricing.Heartbeat' and args.show_heartbeats:
            print heartbeat_to_string(msg)

        if msg_type == "pricing.Price":
            sd = StreamingData(datetime.now(), instrument_string(msg),
                               mid_string(msg), account_api, account_id, 's',
                               '1min', balance)
            df = df.append(sd.df())
            '''
                Re-sample is based on time parameter set in StreamingData().
                i.e., 1min, 5min, 15min, etc.
            '''
            sd.resample(df)

            '''
                This following output is information on the streaming data that has been collected.
                    df.shape[0]: represents the current/cumulative rows of streaming data that has come in.
                    sd.shape[0]: represents the current/cumulative rows related to the time frame being evaluated.
            '''
            # print "df:", df.shape[0], "minuteData:", sd.minuteData().shape[0]
            # print sd.minuteData(), '\n'

            if sd.minuteData().shape[0] < 20:
                continue
            else:
                client = oandapyV20.API(settings.ACCESS_TOKEN)
                r = openPos.OpenPositions(accountID=account_id)
                client.request(r)

                '''
                    Declare array to store open trades so multiple positions aren't established on a single currency.
                '''
                openTrades = []
                for i in r.response['positions']:
                    trades = i['instrument']
                    openTrades.append(trades)
                print 'Open Trades', openTrades

                if instrument_string(msg) in openTrades:
                    continue
                else:
                    try:
                        breakout = Breakout(sd.minuteData(), mid_string(msg))
                        breakout_units = breakout.breakout()
                        if breakout_units is None:
                            pass
                        else:
                            spread = Spreads(dfD, mid_string(msg))
                            pivot, rl1, rl2, rl3, sl1, sl2, sl3 = spread.spreads()
                            rate1, rate2 = spread.spreadRates()
                            strategy = Strategy(
                                instrument_string(msg), dfD, mid_string(msg), breakout_units,
                                pivot, rl1, rl2, rl3, sl1, sl2, sl3, rate1, rate2
                            )

                            if strategy.resistance_check() is None:
                                continue
                            else:
                                units, stop_loss, profit = strategy.resistance_check()
                                try:
                                    resistance_execute = Execute(
                                        account_api, account_id, instrument_string(msg), units, stop_loss, profit
                                    )
                                    resistance_execute.trade()
                                except Exception as e:
                                    print(e)

                            if strategy.support_check() is None:
                                continue
                            else:
                                units, stop_loss, profit = strategy.support_check()
                                try:
                                    support_execute = Execute(
                                        account_api, account_id, instrument_string(msg), units, stop_loss, profit
                                    )
                                    support_execute.trade()
                                except Exception as e:
                                    print(e)

                    except Exception as e:
                        print(e)


if __name__ == "__main__":
    main()
