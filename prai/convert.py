"""Prai conversion library. No need to call RPC for this one"""

__author__ = 'jxub'

RAI_RATIO  = 10 ** 24  # amount of raw in rai
KRAI_RATIO = 10 ** 27  # amount of raw in krai
MRAI_RATIO = 10 ** 30  # amount of raw in mrai


def __answer(self, amount):
    """
    Internal module function for providing a pseudo-RPC
    response as it was from a Raiblocks node.

    :param amount: the converted amount
    :type amount: int
    :return: pseudo json response of converted amount
    :rtype: str
    """
    return '''{ "amount": "{}" }'''.format(str(amount))

def mrai_from_raw(self, raw):
    """
    Divide a raw amount down by the Mrai ratio.
    Equivalent to call "action": "mrai_from_raw".
    Returns Mrai amount

    :param raw: raw amount
    :type raw: int
    :return: mrai amount
    :rtype: str
    """

    mrai = raw // MRAI_RATIO

    return __answer(mrai)


def mrai_to_raw(self, mrai):
    """
    Multiply an Mrai amount by the Mrai ratio.
    Equivalent to call "action": "mrai_to_raw".
    Returns raw amount.

    :param mrai: mrai amount
    :type mrai: int
    :return: raw amount
    :rtype: str
    """

    raw = mrai * MRAI_RATIO

    return __answer(raw)


def krai_from_raw(self, raw):
    """
    Divide a raw amount down by the Krai ratio.
    Equivalent to call "action": "krai_from_raw".
    Returns Krai amount.

    :param raw: raw amount
    :type raw: int
    :return: krai amount
    :rtype: str
    """

    krai = raw // KRAI_RATIO

    return __answer(krai)


def krai_to_raw(self, krai):
    """
    Multiply an Krai amount by the Krai ratio.
    Equivalent to call "action": "krai_to_raw".
    Returns raw amount.

    :param krai: krai amount
    :type krai: int
    :return: raw amount
    :rtype: str
    """

    raw = krai * KRAI_RATIO

    return __answer(raw)


def rai_from_raw(self, raw):
    """
    Divide a raw amount down by the rai ratio.
    Equivalent to call "action": "rai_from_raw".
    Returns Rai amount.

    :param raw: raw amount
    :type raw: int
    :return: rai amount
    :rtype: str
    """

    rai = raw // RAI_RATIO

    return __answer(rai)


def rai_to_raw(self, rai):
    """
    Multiply an rai amount by the rai ratio.
    Equivalent to call "action": "rai_to_raw".
    Returns raw amount.

    :param krai: rai amount
    :type krai: int
    :return: raw amount
    :rtype: str
    """

    raw = rai * RAI_RATIO

    return __answer(raw)
