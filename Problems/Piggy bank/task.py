class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollar, cent):
        self.dollars = 0
        self.cents = 0
        self.add_money(dollar, cent)

    def add_money(self, deposit_dollars, deposit_cents):
        self.cents += deposit_cents
        d = self.cents // 100
        d_rest = self.cents % 100
        self.cents = d_rest
        self.dollars += deposit_dollars
        self.dollars += d
        # print(self.dollars, self.cents)


if __name__ == '__main__':
    # p = PiggyBank(0, 50)
    # p.add_money(0, 99)
    pass
