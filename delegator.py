from base import _call


def get_delegators(account):
    """
    Returns a list of pairs of delegator names given account a representative and its balance

    :param account: account address
    :type account: str
    :return:
    :rtype:
    """

    action = "delegators"

    return _call(action, account=account)


def get_delegator_count(account):
    """
    Get number of delegators for a specific representative account

    :param account: account address
    :type account: str
    :return:
    :rtype:
    """

    action = "delegators_count"

    return _call(action, account=account)
