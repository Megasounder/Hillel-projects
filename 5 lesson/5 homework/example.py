

class Calculator:
    def __init__(self, a=0, b=0) -> None:
        self.a = a
        self.b = b

    def add(self, a, b):
        c = a + b
        return c


class IntegerCalculator(Calculator):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        super().__init__()



    # def add(self, a, b) -> int:
    #     c = int(a) + int(b)
    #     return c


class FloatCalculator(Calculator):
    def super__init__(self) -> None:
        pass


    # def add(self, a, b) -> float:
    #     c = float(a) + float(b)
    #     return c


def make_add(obj, a, b):
    c = obj.add(a, b)
    return c


int_calc = IntegerCalculator()
result = make_add(int_calc, 1.0, 2)
print(result)  # результат має бути 3
float_calc = FloatCalculator ()
result = make_add(float_calc, 1, 2.0)
print(result) # результат має бути 3.0
