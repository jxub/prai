
class Resource:

    def __init__(self, node_uri):
        """
        :param node_uri: the uri of the Rai node
        :type node_url: str
        """
        self.node_uri = node_uri

    def __send(action, wallet=None, key=None, count=None, account=None, accounts=None,
               representative=None, block=None, source=None, destination=None, amount=None,
               threshold=None, _hash=None, weight=None, pending=None):
        """
        Handles the call to the rai node.

        :param action: mandatory param of action type
        :type action: str
        :param count: (optional)
        :type count: int
        :param accounts: (optional) list of account address strings to be moved
        :type accounts: list
        :param work: (optional) disable work generation after account creation
        :type work: bool
        :param representative: (optional) return representative for the account if set to "true",
            also used to set representative if is an address
        :type representative: bool or str
        :param hash: (optional) base64 hash of the block
        :type hash: str
        :param pending: (optional) return voting weight if set to "true"
        :type weight: bool
        :param pending: (optional) return pending balance for account if set to "true"
        :type pending: bool

        # TODO: return a RaiResponse object instead of json
        """
        payload = []
        payload.append('''"action": "{}"'''.format(action))
        if wallet:
            payload.append('''"wallet": "{}"'''.format(wallet))
        if key:
            payload.append('''"key": "{}"'''.format(key))
        if count:
            payload.append('''"count": "{}"'''.format(str(count)))
        if account:
            payload.append('''"account": "{}"'''.format(account))
        if accounts:
            payload.append('''"accounts": "{}"'''.format(accounts))
        if block:
            payload.append('''"block": "{}"'''.format(block))
        if source:
            payload.append('''"source": "{}"'''.format(source))
        if destination:
            payload.append('''"destination": "{}"'''.format(destination))
        if amount:
            payload.append('''"amount": "{}"'''.format(amount))
        if threshold:
            payload.append('''"threshold": "{}"'''.format(threshold))
        if _hash:
            # TODO validate hash len is 64
            payload.append('''"hash": "{}"'''.format(_hash))
        if not work:
            payload.append('''"work": "false"''')
        if representative:
            if isinstance(representative, str):
                payload.append('''"representative": "{}"'''.format(representative))
            else:
                payload.append('''"representative": "true"''')
        if weight:
            payload.append('''"weight": "true"''')
        if pending:
            payload.append('''"pending": "true"''')

        data = "\{{}\}".format(', '.join(payload))

        resp = self.__get_response_dict(data)

        self.__make_response_object(resp)

    def __make_response_object(self, resp):
        """
        Returns a constructed RaiResponse object
        """
        pass

    def __get_response_dict(self, data):
        """
        Sends the string payload and returns a parsed response from the rai node.

        :param data: data to post and parse
        :type data: str
        :returns: response dict
        :rtype: str
        """
        response = requests.post(self.node_uri, data=data)
        if not response.ok:
            return None
        resp_dict = json.loads(response.text)
        return resp_dict


def call(action, **kwargs):
    """
    Call the rai node without subclassing Resource for things like delegators, frontiers etc.

    :param action: mandatory param of action type
    :type action: str
    """
    return Resource.__send(action, **kwargs)


def retrieve_online_peers():
    # TODO
    pass
