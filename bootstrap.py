import json
import requests

def bootstrap(address, port):
    """
    Initialize bootstrap to specific IP address and port

    :param address:
    :type address: str
    :param port: defaults to 7075 if address specified,
    which is the default rai node (TODO check)
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


def _bootstrap(action, address=None, port=7075):
    """
    Internal function that makes the connection

    :return: true if bootstrap was successful, false otherwise
    :rtype: bool
    """
    if address:
        uri = "{}:{}".format(address, str(port))
    else:
        _find_random_peers()

    response = requests.post(self.uri, data=data)
    if not response.ok:
        return False
    resp_dict = json.loads(response.text)

    # success has empty string value, ok then
    if resp_dict["success"] == "":
        return True
    
    return False

def _find_random_peers():
    pass


