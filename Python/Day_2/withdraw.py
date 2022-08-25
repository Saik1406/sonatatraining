from account import LowBalance
def withdraw(balance,amount):
    if(balance<amount):
        raise insufficient("insufficient balance")
    balance=balance-amount

