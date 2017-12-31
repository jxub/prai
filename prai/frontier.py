from base import _call


def get_frontiers(account):
    """
    Returns a list of pairs of account and block hash
    representing the head block starting at account up to count

    :param account: account address
    :type account: str
    :return: list of pairs of account and head block hash
    :rtype: dict
    """

    action = "frontiers"
    
    return _call(action, account=account)


def get_frontier_count(account):
    """
    Reports the number of accounts in the ledger

    :param account: account address
    :type account: str
    :return: number of accounts in ledger
    :rtype: dict
    """

    action = "frontier_count"

    return _call(action, account=account)