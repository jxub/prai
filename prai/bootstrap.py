import json
import requests

from .base import retrieve_online_peers


def bootstrap(address='127.0.0.1', port=7076):
    """
    Initialize bootstrap to specific IP address and port

    :param address: (optional) http address, defaults to localhost
    :type address: str
    :param port: (optional) defaults to 7076 if address specified,
        which is the primary rai activity port
    :type port: str or int
    :return: true if bootstrap was successful, false otherwise
    :rtype: bool
    """

    action = "bootstrap"
    
    return _bootstrap(action, address=address, port=port)


def bootstrap_any():
    """
    Initialize multi-connection bootstrap to random peers

    :return: true if bootstrap was successful, false otherwise
    :rtype: bool
    """

    action = "bootstrap_any"

    return _bootstrap(action)


def _bootstrap(action, address, port):
    """
    Internal function that makes the connection

    :param action: action to be done
    :type action: str
    :param address: (optional) http address
    :type address: str
    :param port: (optional) http port
    :type port: str or int
    :return: true if bootstrap was successful, false otherwise
    :rtype: bool
    """
    uris = []
    if action == 'bootstrap':
        uris.append("{}:{}".format(address, str(port)))
    else:
        uris.append(_find_random_peers())

    for uri in uris:
        response = requests.post(uri, data=data)
        if not response.ok:
            return False
        resp_dict = json.loads(response.text)

        # success has empty string value, ok then
        if resp_dict["success"] != "":
            return False
        
    return True


def _find_random_peers():
    # TOOD mske it work
    peers = retrieve_online_peers()
    return [peer.url for peer in peers]
