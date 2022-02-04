import abc

class Car(abc.ABC):
    def __init__(self, reg_no, brand):
        self.reg_no = reg_no;
        self.brand = brand;

    @abc.abstractmethod
    def Worth(self):
        pass
