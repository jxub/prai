prai 🙏
===========
Raiblocks Python RPC client

Install
-------
A somewhat stable version from pypi:

.. code-block:: bash

    $ pip install prai

Or the most recent master version from Github:

.. code-block:: bash

    $ git clone https://github.com/jxub/prai

Usage
-----
.. code-block:: Python

    >>> from prai import Wallet, Account

    # creating a wallet with the rai node url
    >>> w = Wallet(http://localhost:7475)

    >>> w.account_list()
    {  
        "accounts" : [
        ]
    }

    >>> w.accounts_create(count=2)
    {  
        "accounts": [    
            "xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000",   
            "xrb_1e5aqegc1jb7qe964u4adzmcezyo6o146zb8hm6dft8tkp79za3s00000000"
        ]   
    }

    >>> w.account_balance("xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000")
    {  
        "balance": "10000",  
        "pending": "10000"  
    }

    # using unpacking to pass in the params with *
    >>> w.send(*w.account_list()['accounts'], 10000)
    {  
    "block": "000D1BAEC8EC208142C99059B393051BAC8380F9B5A2E6B2489A277D81789F3F"  
    }

    # query the same account as before
    >>> w.account_balance("xrb_3e3j5tkog48pnny9dmfzj1r16pg8t1e76dz5tmac6iq689wyjfpi00000000")
    {  
        "balance": "0",  
        "pending": "0"  
    }


Some notes
----------
Prai is a work in progress, so expect some rough edges and stay tuned for updates 🙈.

Roadmap
-------
- Finish basic API.
- Add some higher-level features, for example a simple e-commerce payment API.
- Add more validation and tests (ughhh).
- Add hashing of Rai addrsses to shorter to be better for end-user (??!)
🍻 


