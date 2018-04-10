#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:27:31 2017

@author: jonfroiland
"""


class Balance(object):

    def __init__(self, account_api, account_id):
        self.account_api = account_api
        self.account_id = account_id

    def balance(self):
        balance_response = self.account_api.account.summary(self.account_id)
        keys = balance_response.get("account").__dict__.keys()
        values = balance_response.get("account").__dict__.values()
        details = zip(keys, values)
        balance = round(details[17][1]*.01, 2)
        return balance
