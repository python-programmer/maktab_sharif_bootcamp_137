class Balance:
    def __init__(self, card_number, balance, info):
        self.card_number = card_number
        self.__balance = balance # private
        self._info = info

    def deposit(self, value):
        if value > 100000:
            raise ValueError("money laundry")
        self.__balance += value

    def get_balance(self):
        return self.__balance


class HomeBalance(Balance):
    def __init__(self, card_number, balance, info):
        super().__init__(card_number, balance, info)

    # def daily_check(self):
    #     print(f"{self.card_number}: {self._info}, {self.get_balance()}")

    def __daily_check(self):
        print(f"{self.card_number}: {self._info}, {self.get_balance()}")

hadi_balance = HomeBalance("2566-6666", 1000, "disability")
print(hadi_balance._info)

print(f"{hadi_balance.card_number}: {hadi_balance.get_balance()}")
hadi_balance.deposit(250)
print(f"{hadi_balance.card_number}: {hadi_balance.get_balance()}")
hadi_balance.daily_check()