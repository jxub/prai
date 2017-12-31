
class Resource:
    
    def __send(action, wallet=None, key=None, count=None, account=None, accounts=None, 
               representative=None, block=None, source=None, destination=None, amount=None,
               threshold=None, _hash=None,
               weight=None, pending=None):
        """
        :param action: mandatory param of action type
        :type action: str
        :param count:
        :type count: int
        :param accounts: list of account address strings to be moved
        :type accounts: list
        :param work: optionally disable work generation after account creation
        :type work: bool
        :param representative: return representative for the account if set to "true",
        also used to set representative if is an address
        :type representative: bool or str
        :param hash: base64 hash of the block
        :type hash: str
        :param pending: return voting weight if set to "true"
        :type weight: bool
        :param pending: return pending balance for account if set to "true"
        :type pending: bool
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

        response = requests.post(self.node_uri, data=data)
        if not response.ok:
            return None
        resp_dict = json.loads(response.text)
        return resp_dict


def _call(action, **kwargs):
    # TODO call api without subclassing Resource for things like delegators, frontiers etc.
    return Resource.__send(action, **kwargs)
