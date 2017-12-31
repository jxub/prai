from base import _call


def get_available_supply():
    """
    Returns how many rai are in the public supply

    :returns: dict with `available` key
    :rtype: dict
    """

    action = 'available_supply'

    return _call(action)


def send_keepalive(address, port):
    """
    Tells the node to send a keepalive packet to address:port.

    :param address: http address
    :type address: str
    :param port: http port
    :type port: str or int
    :returns: empty dict
    :rtype: dict
    """

    action = 'keepalive'

    return _call(action, address=address, port=port)


def republish(_hash):
    """
    Rebroadcast blocks starting at hash to the network

    :param _hash: hex block hash
    :type _hash: str
    :returns: dict with `blocks` key and a list of blocks as value
    :rtype: dict
    """
