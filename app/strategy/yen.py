#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:11:52 2017

@author: jonfroiland
"""
from breakout import Breakout
from spreads import Spreads
from resistance import Resistance
from support import Support
from execute.order_response import print_order_create_response_transactions


class Yen(object):

    def __init__(self, api, account_id, instrument, dfD, data, mid):
        self.api = api
        self.account_id = account_id
        self.instrument = instrument
        self.dfD = dfD
        self.data = data
        self.mid = mid
        self.breakout = self.breakout()
        self.pivot, self.rl1, self.rl2, self.rl3, \
            self.sl1, self.sl2, self.sl3 = self.spreads()
        self.rate1, self.rate2 = self.spreadRates()
        self.loss = self.res_check()
        self.loss = self.sup_check()

    def breakout(self):
        try:
            b = Breakout(self.data, self.mid)
            breakout = b.breakout
            return breakout
        except Exception as e:
            print e

    def spreads(self):
        try:
            s = Spreads(self.dfD, self.mid)
            pivot, rl1, rl2, rl3, sl1, sl2, sl3 = s.spreads()
            pivot = round(pivot, 3)
            rl1 = round(rl1, 3)
            rl2 = round(rl2, 3)
            rl3 = round(rl3, 3)
            sl1 = round(sl1, 3)
            sl2 = round(sl2, 3)
            sl3 = round(sl3, 3)
            return pivot, rl1, rl2, rl3, sl1, sl2, sl3
        except Exception as e:
            print e

    def spreadRates(self):
        try:
            s = Spreads(self.dfD, self.mid)
            rate1, rate2 = s.spreadRates()
            return rate1, rate2
        except Exception as e:
            print e

    def res_check(self):
        if self.mid > self.dfD.iloc[-1]['D Pivot Point']:
            print '**** Checking Resistance Pivots ****'
            try:
                res = Resistance(self.instrument, self.mid, self.dfD,
                                 self.breakout, self.pivot, self.rl1, self.rl2,
                                 self.rl3, self.rate1, self.rate2)
            # print res.resistance()
                resLoss = res.resistance()
                loss = float(round(resLoss+.025, 3))
                return loss
            except:
                pass

    def sup_check(self):
        if self.mid < self.dfD.iloc[-1]['D Pivot Point']:
            print '**** Checking Support Pivots ****'
            try:
                sup = Support(self.instrument, self.mid, self.dfD, self.units,
                              self.pivot, self.sl1, self.sl2, self.sl3,
                              self.rate1, self.rate2)
            # print sup.support()
                supLoss = sup.support()
                loss = float(round(supLoss+.025, 3))
                return loss
            except:
                pass

    def trade(self):
        try:
            response = self.api.order.market(
                    self.account_id,
                    instrument=self.instrument,
                    units=self.breakout
            )
            tradeID = response.get('lastTransactionID')
            keys = response.get('orderFillTransaction').__dict__.keys()
            values = response.get('orderFillTransaction').__dict__.values()
            orderFill = zip(keys, values)
            # print orderFill[6]
            if self.units > 0:
                profit = float(round(orderFill[6][1] + .1, 3))
                # print 'LONG PROFIT:', profit
            else:
                profit = float(round(orderFill[6][1] - .1, 3))
                # print 'SHORT PROFIT:', profit
            print("Response: {} ({})".format(
                    response.status, response.reason))
            print("")
            print_order_create_response_transactions(response)

            profit_response = self.api.order.take_profit(
                    self.account_id,
                    instrument=self.instrument,
                    tradeID=tradeID,
                    price=profit
            )

            print("Profit Response: {} ({})".format(
                    profit_response.status, profit_response.reason))
            print("")
            print_order_create_response_transactions(profit_response)

            stop_response = self.api.order.stop_loss(
                    self.account_id,
                    instrument=self.instrument,
                    tradeID=tradeID,
                    price=self.loss
            )
            print("Loss Response: {} ({})".format(
                    stop_response.status, stop_response.reason))
            print("")
            print_order_create_response_transactions(stop_response)
        except:
            pass
