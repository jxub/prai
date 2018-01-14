"""
Prai Raiblocks wallet
"""

import json
import requests

from .base import Resource

__author__ = 'jxub'


class Wallet(Resource):

    def __init__(self, _node_uri):
        self.node_uri = _node_uri # use __send at RaiNode Level
        self.id = self.create()["wallet"]

    def create(self):
        """
        Creates a new random wallet id.
        """
        action = "wallet_create"

        return self.__send(action)

    def get_work(self):
        """
        Returns a list of pairs of account and work from wallet.
        """
        action = "wallet_work_get"

        return self.__send(action)

    def get_representative(self):
        """
        Returns the default representative for wallet
        """
        action = "wallet_representative"

        return self.__send(action, wallet=self.id)

    def set_representative(self, representative):
        """
        Sets the default representative for wallet.
        """
        action = "wallet_representative_set"

        return self.__send(action, wallet=self.id, representative=representative)

    def get_representatives_all(self):
        """
        Returns a list of pairs of representative and its voting weight.
        """
        action = "representatives"

        return self.__send(action)

    def add_key(self, key):
        """
        Add an adhoc private key to wallet.
        """
        action = "wallet_add"

        return self.__send(action, wallet=self.id, key=key)

    def balances(self):
        """
        Returns how many rai is owned and how many have not yet been received by all accounts in wallet.
        """
        action = "wallet_balances"

        return self.__send(action, wallet=self.id)

    def balances_total(self):
        """
        Returns the sum of all accounts balances in wallet.
        """
        action = "wallet_balance_total"

        return self.__send(action, wallet=self.id)

    def search_pending(self):
        """
        Tells the node to look for pending blocks for any account in wallet.
        """
        action = "search_pending"

        return self.__send(action, wallet=self.id)

    def wallet_pending(self, count=100):
        """
        Returns a list of block hashes which have not yet been received by accounts in this wallet.
        """
        action = "wallet_pending"

        return self.__send(action, wallet=self.id, count=count)

    def receive(self, account, block):
        """
        Receive pending block for account in wallet.
        """
        action = "receive"

        return self.__send(action, wallet=self.id, account=account, block=block)

    def send(self, source, destination, amount):
        """
        Send amount from source in wallet to destination.
        """
        action = "send"

        return self.__send(action, wallet=self.id, source=source,
                           destination=destination, amount=amount)

    def accounts_list(self):
        """
        Lists all the accounts inside wallet.
        """
        action = "account_list"

        return self.__send(action, wallet=self.id)
    
    def accounts_move(self, source, accounts):
        """
        Moves accounts from source to wallet.
        """
        action = "account_move"

        if len(source) != 64:
            raise Exception("source account address invalid")

        return self.__send(action, wallet=self.id, source=source)

    def account_remove(self, account):
        """
        Remove account from wallet.
        """
        action = "account_remove"

        return self.__send(action, wallet=self.id, account=account)

    def accounts_balances(self, accounts):
        """
        Returns how many RAW is owned and how many have not yet been received by accounts list.

        :param accounts: list of one or many accounts
        :type accounts: list
        """
        action = "accounts_balances"

        return self.__send(action, accounts=accounts)

    def accounts_create(self, count=1, work=True):
        """
        Creates new accounts, insert next deterministic keys in wallet up to count.
        Disables work generation after creating account if work is set to false.

        :param count: (optional) number of accounts to create, 1 default
        :type count: int
        """
        action = "accounts_create"

        return self.__send(action, wallet=self.id, count=count, work=work)

    def account_create(self, work=True):
        """
        Wrapper for creating a single account
        """
        return self.accounts_create(count=1, work=work)

    def account_balance(self, account):
        """
        Wrapper for querying  a single account
        :param account: account to query
        :type account: str
        """
        return self.accounts_balances([account])
