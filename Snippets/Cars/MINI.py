import Car as c

class MINI(c.Car):
    def __init__(self,reg_no, worth):
        super().__init__(reg_no, "MINI")
        self.worth = worth

    def Worth(self):
        return self.worth