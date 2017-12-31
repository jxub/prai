from .base import _call


def get_node_versions():
    """
    Returns rpc, store, and node vendor version numbers

    :returns: dict of `rpc_version`, `store_version` and `node_vendor`
    :rtype: dict
    """

    action = 'version'

    return _call(action)


def stop_node():
    """
    Stops the raiblocks node

    :returns: dict of `success` key and empty value
    :rtype: dict
    """

    action = 'stop'

    return _call(action)
