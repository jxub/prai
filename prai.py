import json
import random
from configparser import SafeConfigParser
from functools import wraps

import requests



class RaiNode:
    """
    wallet -> accounts
    general
    helpers
    """

    def __init__(self, uri):
        self.uri = uri
        self.wallets = None

    def generate_seed(self):
        #Generates a seed randomly

        seed0x = hex(random.SystemRandom().getrandbits(256))
        seed = seed0x[2:].upper()

        return seed

    def __send(self, data):
        #Sends off POST request to rai_node, returns dict result.
        
        response = requests.post(self.uri, data=data)
        if not response.ok:
            return None
        resp_dict = json.loads(response.text)
        return resp_dict

    def block_count(self):
        #Reports the number of blocks in the ledger and unchecked synchronizing blocks
        action = "block_count"

        request = '''{ "action":"{}" }'''.format(action)

        return self.__send(request)

    def deterministic_key(self, seed, index):
        #Derive deterministic keypair from seed based on index
        action = "deterministic_key"

        request = '''{ "action":"{}", "seed":"{}", "index":"{}" }'''.format(action, seed, index)

        return self.__send(request)

    def wallet_create(self):
        #Creates a new random wallet id
        action = "wallet_create"

        request = '''{ "action":"{}" }'''.format(action)

        return self.__send(request)

    def wallet_add(self, wallet, key):
        #Add an adhoc private key key to wallet
        action = "wallet_add"

        request = '''{ "action":"{}", "wallet":"{}", "key":"{}" }'''.format(action, wallet, key)

        return self.__send(request)

    def wallet_balances(self, wallet):
        #Returns how many rai is owned and how many have not yet been received by all accounts in wallet
        action = "wallet_balances"

        request = '''{ "action":"{}", "wallet":"{}" }'''.format(action, wallet )

        return self.__send(request)

    def account_list(self, wallet):
        #Lists all the accounts inside wallet
        action = "account_list"

        request = '''{ "action":"{}", "wallet":"{}" }'''.format(action, wallet )

        return self.__send(request)

    def account_get(self, key):
        #Get account number for the public key
        action = "account_get"

        request = '''{ "action":"{}", "key":"{}" }'''.format(action, key )

        return self.__send(request)

    def account_balance(self, account):
        #Returns how many RAW is owned and how many have not yet been received by account
        action = "account_balance"

        request = '''{ "action":"{}", "account":"{}" }'''.format(action, account)

        return self.__send(request)

    def account_info(self, account):
        # Returns frontier, open block, change representative block, balance,
        # last modified timestamp from local database & block count for account
        action = "account_info"
        
        request = '''{ "action":"{}", "account":"{}" }'''.format(action, account)

        return self.__send(request)

    def search_pending(self, wallet):
        #Tells the node to look for pending blocks for any account in wallet
        action = "search_pending"

        request = '''{ "action":"{}", "wallet":"{}" }'''.format(action, wallet )

        return self.__send(request)

    def wallet_pending(self, wallet, count = 100):
        #Returns a list of block hashes which have not yet been received by accounts in this wallet
        action = "wallet_pending"

        request = '''{ "action":"{}", "wallet":"{}", "count":"{}" }'''.format(action, wallet, count)

        return self.__send(request)

    def receive(self, wallet, account, block):
        #Receive pending block for account in wallet
        action = "receive"

        request = '''{ "action":"{}", "wallet":"{}", "account":"{}", "block":"{}" }'''.format(action, wallet, account, block)

        return self.__send(request)

    def send(self, wallet, source, destination, amount):
        #Send amount from source in wallet to destination
        action = "send"

        request = '''{ "action":"{}", "wallet":"{}", "source":"{}", "destination":"{}", "amount":"{}" }'''.format(action, wallet, source, destination, amount)

        return self.__send(request)

    def mrai_from_raw(self, amount):
        #Divide a raw amount down by the Mrai ratio.
        action = "mrai_from_raw"

        request = '''{ "action":"{}", "amount":"{}" }'''.format(action, amount)

        return self.__send(request)

    def mrai_to_raw(self, amount):
        #Multiply an Mrai amount by the Mrai ratio.
        action = "mrai_to_raw"

        request = '''{ "action":"{}", "amount":"{}" }'''.format(action, amount)

        return self.__send(request)

    def krai_from_raw(self, amount):
        #Divide a raw amount down by the Krai ratio.
        action = "krai_from_raw"

        request = '''{ "action":"{}", "amount":"{}" }'''.format(action, amount)

        return self.__send(request)

    def krai_to_raw(self, amount):
        #Multiply an Krai amount by the Krai ratio.
        action = "krai_to_raw"

        request = '''{ "action":"{}", "amount":"{}" }'''.format(action, amount)

        return self.__send(request)

    def rai_from_raw(self, amount):
        #Divide a raw amount down by the rai ratio.
        action = "rai_from_raw"

        request = '''{ "action":"{}", "amount":"{}" }'''.format(action, amount)

        return self.__send(request)

    def rai_to_raw(self, amount):
        #Multiply an rai amount by the rai ratio.
        action = "rai_to_raw"

        request = '''{ "action":"{}", "amount":"{}" }'''.format(action, amount)

        return self.__send(request)

    def wallet_representative(self, wallet):
        #Returns the default representative for wallet
        action = "wallet_representative"

        request = '''{ "action":"{}", "wallet":"{}" }'''.format(action, wallet)

        return self.__send(request)

    def wallet_representative_set(self, wallet, representative):
        #Sets the default representative for wallet
        action = "wallet_representative_set"

        request = '''{ "action":"{}", "wallet":"{}", "representative":"{}" }'''.format(action, wallet, representative)

        return self.__send(request)

    def history(self, hash, count = 1):
        #Reports send/receive information for a chain of blocks
        action = "history"

        request = '''{ "action":"{}", "hash":"{}", "count":"{}" }'''.format(action, hash, count)

        return self.__send(request)


def validate(node_func):
    
    @wraps(node_func)
    def wrapper(*args, **kwargs):
        amount = args[0]
        try:
            num_amount = int(amount)
        except ValueError:
            return {"message":"ERROR (amount not a number representation)"}
        
        if num_amount < 0:
            return {"message":"ERROR (amount is negative)"}
        res = node_func(amount)

        return {"result":res["amount"]}

class NodeParser:

    @validate
    def returnMraiFromRaw(self, amount):
        return node.mrai_from_raw(amount)

    @validate
    def returnMraiToRaw(self, amount):
        r = node.mraiToRaw(amount)
        return {"result":r["amount"]}

    @validate
    def returnKraiFromRaw(self, amount):
        r = node.krai_from_raw(amount)
        return {"result":r["amount"]}

    @validate
    def returnKraiToRaw(self, amount):
        r = node.krai_to_raw(amount)
        return {"result":r["amount"]}

    @validate
    def returnRaiFromRaw(self, amount):
        r = node.rai_from_raw(amount)
        return {"result":r["amount"]}

    def returnRaiToRaw(self, amount):
        if(not amount.isnumeric()):
            return {"message":"ERROR"}
        elif(int(amount) < 0):
            return {"message":"ERROR"}
        r = node.rai_to_raw(amount)
        return {"result":r["amount"]}

    def returnAccountBalance(self, account):
        #Returns an account balance as a string
        balance = node.account_balance(account)
        try:
            ab = str(node.rai_from_raw(balance["balance"])["amount"])
            ab = list(ab)
            if(len(ab) > 6):
                ab.insert(-6, ".")
            ab = "".join(ab)
            return {"balance":ab}
        except:
            return balance
    #end returnAccountBalance

    def returnNewSeed(self):
        seed = node.generate_seed()
        return {"seed":seed}

    def returnNewWallet(self):
        wallet = node.wallet_create()
        return wallet

    def createWalletSet(self, seed, wallet_number, index):
        #Creates a wallet set with 5 important tokens, must be saved
        try:
            dk = node.deterministic_key(seed, index)
            private = dk["private"]
            public = dk["public"]
            account = dk["account"]
            self.insertAccountInWallet(wallet_number, private)
        except:
            return {"message":"ERROR"}
        
        wset = { "seed":seed, "wallet":wallet_number, "private":private, "public":public, "account":account }

        return wset
    #end createWalletSet

    def insertAccountInWallet(self, wallet, private):
        try:
            json = node.wallet_add(wallet, private)
            try:
                key = json["account"]
                return {"message":"OK"}
            except:
                key = json["error"]
                return {"message":"ERROR"}
        except:
            return {"message":"ERROR"}

    def createNewAccount(self, seed, wallet, index):
        dk = node.deterministic_key(seed, index)

        try: 
            private = dk["private"]
            public = dk["public"]
            account = dk["account"]
            self.insertAccountInWallet(wallet, private)
        except:
            return dk

        wset = {"private":private, "public":public, "account":account }

        return wset
    #end createNewAccount

    def receiveAllXrb(self, wallet):
        #Routine to start a receive on every pending block, and returns a log with the received blocks
        node.search_pending(wallet)
        pending = node.wallet_pending(wallet)

        try:
            blocks = pending["blocks"]
        except:
            return pending

        log = {}

        for acc in blocks:
            log[acc] = []
            for b in blocks[acc]:
                node.receive(wallet,acc, b)
                log[acc].append( {"block":b, "amount":node_parser.checkBlockHistory(b)["history"][0]["amount"]} )

        return log
    #end receiveAllXrb

    def sendXrb(self, wallet, source, destination, amount):
        #Sends a value from a source to a destination, returns the block, the amount and the accounts as a log
        block = node.send(wallet, source, destination, amount)
        try: 
            block = block["block"]
            log = { "block":block, "amount":amount, "source":source, "destination":destination }
        except:
            log = block
        return log
    #end sendXrb

    def returnRepresentative(self, wallet):
        #Returns the representative account of a wallet
        return node.wallet_representative(wallet)
    #end getRepresentative

    def changeRepresentative(self, wallet, representative):
        #Sets the presentative account of a wallet
        s = node.wallet_representative_set(wallet, representative)
        try:
            s = s["set"]
            rep = { "set":s, "representative":representative }
        except:
            rep = s
        return rep
    #end setRepresentative

    def checkBlockHistory(self, block):
        #Returns a block history
        return node.history(block)
    #end checkBlockHistory

#------------------------------------------------------#

config_parser = SafeConfigParser()
config_files = config_parser.read('config.ini')
uri = config_parser.get("rai_node","uri")

node = RaiNode(uri)
node_parser = NodeParser()
