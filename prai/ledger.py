from .base import _call


def get_ledger(account, count=1, representative=False, weight=False,
               pending=False, sorting=False):
    """
    Returns frontier, open block, change representative block,
    balance, last modified timestamp from local database and
    block count starting at account up to count

    :param account: account address
    :type account: str
    :param count: number of blocks to return, 1 default
    :type count: int
    :param representative: return representative (optional)
    :type representative: bool
    :param weight: return weight (optional)
    :type weight: bool
    :param pending: return pending balance (optional)
    :type pending: bool
    :param sorting: return in descending order (optional)
    :type sorting: bool
    :return: ledger
    :rtype: dict
    """

    action = 'ledger'

    return _call(action, account=account, count=count,
                 representative=representative, weight=weight,
                 pending=pending, sorting=sorting)
