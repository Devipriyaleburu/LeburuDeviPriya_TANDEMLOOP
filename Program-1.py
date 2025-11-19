#USING PYTHON LANGUAGE SMALL CALCULATOR
class Calculator:
    def calculate(self, a, b, ope):
        if ope == "addition":
            return a + b
        elif ope == "subtraction":
            return a - b
        elif ope == "multiplication":
            return a * b
        elif ope== "division":
            if b != 0:
                return a / b
            else:
                return "zero division error"
        else:
            return "Given inputs are not valid"
c= Calculator()
print(c.calculate(10, 5, "addition"))
print(c.calculate(10, 5, "subtraction"))
print(c.calculate(10, 5, "multiplication"))
print(c.calculate(10, 5, "division"))


