class Calculator:
    def __init__(self, a: int, b: int, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def cal(self):
        if self.operation == "Addition":
            return self.a + self.b
        elif self.operation == "Subtraction":
            return self.a - self.b
        elif self.operation == "Multiplication":
            return self.a * self.b
        elif self.operation == "Division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error:Division By Zero"
        else:
            return "Error:Invalid Operation"


# 
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
operation = input("Enter Operation (Addition, Subtraction, Multiplication, Division): ")

calc = Calculator(a, b, operation)
result = calc.cal()

print("Result:", result)
