class Balance:
    def __init__(self, card_number, balance, info):
        self.card_number = card_number # public
        self.__balance = balance # private
        self._info = info # protected

    def deposit(self, value): # setter
        if value > 100000:
            raise ValueError("money laundry")
        self.__balance += value

    def get_balance(self): # getter
        return self.__balance

    # top hard skills
    @property
    def info(self):
        prefix = "IR690"
        return f"{prefix}{self._info}"

    @info.setter
    def info(self, value):
        raise ValueError("You can't set value for this field")
        # if len(value) < 4:
        #     raise ValueError("This is invalid")
        # self._info = value




class HomeBalance(Balance):
    def __init__(self, card_number, balance, info):
        super().__init__(card_number, balance, info)

    # def daily_check(self):
    #     print(f"{self.card_number}: {self._info}, {self.get_balance()}")

    def __daily_check(self):
        print(f"{self.card_number}: {self._info}, {self.get_balance()}")

hadi_balance = HomeBalance("2566-6666", 1000, "disability")
print(hadi_balance._info)

hadi_balance.balance = 900

print(f"{hadi_balance.card_number}: {hadi_balance.balance}")
hadi_balance.deposit(250) # setter
print(f"{hadi_balance.card_number}: {hadi_balance.get_balance()}") # getter
# hadi_balance.daily_check()


print(f"{hadi_balance.info}")

hadi_balance.info = "abcd"

print(f"{hadi_balance.info}")