import Car as c

class AUDI(c.Car):
    def __init__(self, reg_no, worth):
        super().__init__(reg_no, "AUDI")
        self.worth = worth

    def Worth(self):
        return self.worth