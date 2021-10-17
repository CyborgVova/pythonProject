class Human:
    pass

    def __init__(self, income=0, balance=0, spend=0, total_income=0, total_spend=0):
        self.income = income
        self.spend = spend
        self.balance = balance
        self.total_income = total_income
        self.total_spend = total_spend

    def keeper(self):
        if self.balance >= self.spend:
            self.balance = self.balance + self.income - self.spend
            self.total_income += self.income
            self.total_spend += self.spend
            self.income = 0
            self.spend = 0
        else:
            self.income = 0
            self.spend = 0
            print('Недостаточно средств')
        return print('Баланс:', self.balance, 'руб.')
