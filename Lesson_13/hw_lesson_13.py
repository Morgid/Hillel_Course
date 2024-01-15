class AmountGreaterHundred:
    def __init__(self, amount):
        self.amount = amount

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        if (self.amount + other.amount) > 100:
            return True
        else:
            return False


object_1 = AmountGreaterHundred(59)
object_2 = AmountGreaterHundred(42)

print(object_1 > object_2)
