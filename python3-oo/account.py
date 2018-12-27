class Account:
    bank_code = "001"

    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def print_balance(self):
        print("Current balance: {}".format(self.__balance))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__may_withdraw(value):
            self.__balance -= value
        else:
            print("The value ({}) is greater than your limit".format(value))

    def transfer(self, value, destiny_account):
        self.withdraw(value)
        destiny_account.deposit(value)

    def __may_withdraw(self, value_to_withdraw):
        value_available_to_withdraw = self.__balance + self.__limit
        return value_to_withdraw <= value_available_to_withdraw

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
