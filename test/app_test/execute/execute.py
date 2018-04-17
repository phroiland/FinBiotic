#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:17:12 2017

@author: jonfroiland
"""
from order_response import print_order_create_response_transactions


class Execute(object):

    def __init__(self, api, account_id, instrument, units, loss):
        self.api = api
        self.account_id = account_id
        self.instrument = instrument
        self.units = units
        self.loss = loss

    def trade(self):
        response = self.api.order.market(self.account_id,
                                         instrument=self.instrument,
                                         units=self.units)
        tradeID = response.get('lastTransactionID')
        keys = response.get('orderFillTransaction').__dict__.keys()
        values = response.get('orderFillTransaction').__dict__.values()
        orderFill = zip(keys, values)
        # print orderFill[6]
        if self.units > 0:
            profit = float(round(orderFill[6][1] + .0005, 5))
            loss = float(round(orderFill[6][1] - .0005, 5))
            # print 'LONG PROFIT:', profit
        else:
            profit = float(round(orderFill[6][1] - .0005, 5))
            loss = float(round(orderFill[6][1] + .0005, 5))
            # print 'SHORT PROFIT:', profit
        print "Response: {} ({})".format(response.status, response.reason)
        print ""
        print_order_create_response_transactions(response)

        profit_response = self.api.order.take_profit(
                self.account_id, instrument=self.instrument, tradeID=tradeID,
                price=profit)

        print "Profit Response: {} ({})".format(
                profit_response.status, profit_response.reason)
        print ""
        print_order_create_response_transactions(profit_response)

        stop_response = self.api.order.stop_loss(
                self.account_id, instrument=self.instrument, tradeID=tradeID,
                price=loss)
        print "Loss Response: {} ({})".format(
                stop_response.status, stop_response.reason)
        print ""
        print_order_create_response_transactions(stop_response)
