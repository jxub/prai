from base import _call


def deterministic_key(seed, index):
    """
    Derive deterministic keypair from seed based on index

    :param seed: a securely generated hexadecimal seed of length 64
    :type seed: str
    :param index: number of permutations (check)
    :type index: int
    """


def create_key():
    """
    Generates an adhoc random keypair

    :return: private and public keys and account values
    :rtype: dict
    """

    action = 'key_create'

    return _call(action)


def expand_key(key):
    """
    Derive public key and account number from private key

    :param key: the base16 key to expand of length 64
    :type key: str
    :return: private and public keys and account values
    :rtype: dict
    """

    action = 'key_expand'

    return _call(action, key)
