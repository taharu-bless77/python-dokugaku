class Bank:
    def __init__(self, amounts, name):
        self._amounts = amounts.copy()
        self._name = name

    def transfer(self, sender, receiver, yen):
        self._amounts[sender] -= yen
        self._amounts[receiver] += yen

    def withdraw(self, name, yen):
        

    