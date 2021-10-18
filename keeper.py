class Human:
    def __init__(self, income=0, balance=0, spend=0, total_income=0, total_spend=0):
        self.income = income
        self.spend = spend
        self.__balance = balance
        self.__total_income = total_income
        self.__total_spend = total_spend

    @property
    def keeper(self):
        if self.__balance >= self.spend:
            self.__balance = self.__balance + self.income - self.spend
            self.__total_income += self.income
            self.__total_spend += self.spend
            self.income = 0
            self.spend = 0
        else:
            self.income = 0
            self.spend = 0
            print('Недостаточно средств')
        return print('Баланс:', self.__balance, 'руб.')

    @property
    def total_income(self):
        return print('Общий доход:', self.__total_income, 'руб.')

    @property
    def total_spend(self):
        return print('Общий расход:', self.__total_spend, 'руб.')
