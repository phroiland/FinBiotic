#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:30:38 2017

@author: jonfroiland
"""
# Standard Imports
import argparse
import common.config
import common.args
import oandapyV20
import oandapyV20.endpoints.positions as openPos

from datetime import datetime
import pandas as pd
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.max_columns', 0)
import sys
import settings

# Data, Price, and Strategy Imports
from streamingData import StreamingData
from balance import Balance
from breakout import Breakout
from spreads import Spreads
from strategy import Strategy
from pivotImports import PivotImports
from view import mid_string, heartbeat_to_string, instrument_string
#from view import bid_string, ask_string, price_to_string

def main(): 
    print "------ System online -------", datetime.now()

    parser = argparse.ArgumentParser()

    common.config.add_argument(parser)
    
    parser.add_argument(
        '--instrument', "-i",
        type=common.args.instrument,
        required=True,
        action="append",
        help="Instrument to get prices for"
    )
    
    parser.add_argument(
        '--snapshot',
        action="store_true",
        default=True,
        help="Request an initial snapshot"
    )

    parser.add_argument(
        '--no-snapshot',
        dest="snapshot",
        action="store_false",
        help="Do not request an initial snapshot"
    )

    parser.add_argument(
        '--show-heartbeats', "-s",
        action='store_true',
        default=False,
        help="display heartbeats"
    )

    args = parser.parse_args()
    #print sys.argv[2]
    account_id = args.config.active_account
    api = args.config.create_streaming_context()
    account_api = args.config.create_context()
   
    response = api.pricing.stream(
        account_id,
        snapshot=args.snapshot,
        instruments=",".join(args.instrument)
    )
    
    p = PivotImports(sys.argv[2], datetime.now().date())
    dfD = p.daily()
    #dfW = p.weekly()
    bal = Balance(account_api, account_id)
    balance = bal.balance()
    
    df = pd.DataFrame([])
        
    for msg_type, msg in response.parts():
        if msg_type == "pricing.Heartbeat" and args.show_heartbeats:
            print(heartbeat_to_string(msg))
            
        if msg_type == "pricing.Price":
            sd = StreamingData(datetime.now(),instrument_string(msg),
                               mid_string(msg),account_api,account_id,
                               's','1min',balance)
            df = df.append(sd.df())
            sd.resample(df)
            print "df:",df.shape[0], "minuteData:",sd.minuteData().shape[0]
            #print sd.minuteData(),'\n'
            
            if sd.minuteData().shape[0]<20:continue
            
            else:
                client = oandapyV20.API(settings.ACCESS_TOKEN)
                r = openPos.OpenPositions(accountID=account_id)
                client.request(r)
                openTrades = []
                for i in r.response['positions']:
                    trades = i['instrument']
                    openTrades.append(trades)    
                print 'Open Trades', openTrades
                
                if instrument_string(msg) in openTrades:continue
                
                else:
                    try:
                        b = Breakout(sd.minuteData(),mid_string(msg))
                        breakout = b.breakout()
                        #print 'Breakout Units:',breakout
                        
                        s = Spreads(dfD,mid_string(msg))
                        pivot, rl1, rl2, rl3, sl1, sl2, sl3 = s.spreads()
                        rate1, rate2 = s.spreads_out()
                        
                        strat = Strategy(account_api,account_id,
                                         instrument_string(msg),dfD,
                                         mid_string(msg),breakout,pivot,
                                         rl1,rl2,rl3,sl1,sl2,sl3,rate1,rate2)
                        strat.res_check()
                        strat.sup_check()

                    #except Exception as e: print(e)
                    except:continue
                        
if __name__ == "__main__":
    main()