    
class Account(Resource):
    
    def __init__(self, wallet, key=None):
        # id of the wallet that owns account
        self.wallet = wallet

        # account exists
        if key:
            self.id = self.get()["account"]
        # or not
        else:
            self.id = self.create()["account"]

    def get_balance(self):
        # Returns how many RAW is owned and how many have not yet been received by account
        action = "account_balance"

        return self.__send(action, account=self.id)

    def get_block_count(self):
        # Get number of blocks for a specific account
        action = "account_block_count"

        return self.__send(action, account=self.id)

    def get_info(self, representative=None, weight=None, pending=None):
        # Returns frontier, open block, change representative block, balance,
        # last modified timestamp from local database & block count for account
        # Additionally returns representative, voting weight, pending balance for account
        # if any of this params is set to true
        action = "account_info"

        return self.__send(action, account=self.id,
                           representative=representative,
                           weight=weight, pending=pending)

    def create(self, work=True):
        # Creates a new account, insert next deterministic key in wallet
        # Disables work generation after creating account if work is set to False

        action = "account_create"

        return self.__send(action, wallet=self.wallet, work=work)

    def get(self, key):
        # Get account number for the public key
        action = "account_get"

        return self.__send(action, key=key)
    
    def history(self, count=1):
        # Reports send/receive information for a account
        action = "account_history"

        return self.__send(action, account=self.id, count=count)

    def get_public_key(self):
        # Get the public key for account
        action = "account_key"

        return self.__send(action, account=self.id)

    def get_representative(self):
        # Returns the representative for account
        action = "account_representative"

        return self.__send(action, account)

    """
    better inside wallet
    def account_list(self, wallet):
        # Lists all the accounts inside wallet
        action = "account_list"

        return self.__send(action, wallet=self.wallet)
    def move(self, source, accounts):
        # Moves accounts from source to wallet
        action = "account_move"

        return self.__send(action, wallet=self.wallet, source=source)
    def remove(self):
        # Remove account from wallet
        action = "account_remove"

        return self.__send(action, wallet=self.wallet, account=self.id)
    """

