from base import _call

def get_delegators(account):
    # Returns a list of pairs of delegator names given account a representative and its balance
    action = "delegators"
    
    return _call(action, account)

def get_delegator_count(account):
    # Get number of delegators for a specific representative account
    action = "delegators_count"

    return _call(action, account)
