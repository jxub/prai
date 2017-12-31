from base import Resource

class Block(Resource):
    def __init__(self, _hash):
        """
        :param _hash: base64 hash
        :type _hash: str
        """
        self.hash = _hash
    
    def get_account(self):
        # Returns the account containing block
        action = "block_account"

        self.__send(action, _hash=self.hash)
    
    # TODO block_count and block_count_type in Ledger class
    # TODO block_create, process and receive (block) in Account class
    # blocks and blocks_info (retrieve many blocks) in a Manager class

    def get_chain(self, count=1):
        # Returns a list of block hashes in the account chain starting at block up to count
        action = "chain"

        self.__send(action, block=self.hash, count=count)
