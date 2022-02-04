import Car as c

class BMW(c.Car):
    def __init__(self, reg_no, worth):
        super().__init__(reg_no,"BMW")
        self.worth = worth

    def Worth(self):
        return self.worth