class Bank:
    def __init__(self, amounts, name):
        self._amounts = amounts.copy()
        self._name = name

    def transfer(self, sender, receiver, yen):
        self._amounts[sender] -= yen
        self._amounts[receiver] += yen

    def withdraw(self, name, yen):
        if self._amounts[name] >= yen:
            self._amounts[name] -= yen
            return self._amounts[name]
        else:
            return None

# 使用例
bank = Bank({
    'alice': 1000000,
    'bob': 1234,
    'shop': 100000
}, 'MyBank')

bank.transfer('alice', 'bob', 300)
bank.transfer('bob', 'shop', 10000)

print(bank.withdraw('alice', 50000))  # 'alice'の残高を表示
print(bank.withdraw('bob', 5000))     # 残高不足のためNoneを表示s