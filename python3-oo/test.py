def create_account(number, holder, balance, limit):
    return {"number": number, "holder": holder, "balance": balance, "limit": limit}


def deposit(account, value):
    account["balance"] += value


def withdraw(account, value):
    account["balance"] -= value


def print_balance(account):
    print("Balance: {}".format(account["balance"]))
