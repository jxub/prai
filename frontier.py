from base import _call


def get_frontiers(account):
    """
    Returns a list of pairs of account and block hash
    representing the head block starting at account up to count
    """

    action = "frontiers"
    
    return _call(action, account)


def get_frontier_count(account):
    """
    Reports the number of accounts in the ledger
    """

    action = "frontier_count"

    return _call(action, account)