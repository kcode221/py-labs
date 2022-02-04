import Car as c

class JLR(c.Car):
    def __init__(self, reg_no, worth):
        super().__init__(reg_no, "JLR")
        self.worth = worth

    def Worth(self):
        return self.worth