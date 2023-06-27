"""
Exercise 2 (Polymorphism - OverloadingII- Math):
Create a Python class called MathOperations with overloaded
methods for:
addition (add()),
subtraction (subtract()), and
multiplication (multiply()).
Each method should take different numbers of arguments
and perform the corresponding operation.
In your main() function, create an instance of the MathOperations
class and demonstrate the polymorphic behavior by calling each method
with different numbers of arguments.

"""
print("_____________________________________________")

# Solution

class MathOperations:
    def add(self, *args):
        result = sum(args)
        return result

    def subtract(self, *args):
        if len(args) < 2:
            raise ValueError("Subtraction requires at least two arguments.")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result


def main():
    math_ops = MathOperations()

    # Addition
    result = math_ops.add(2, 3)
    print(f"Addition Result: {result}")

    result = math_ops.add(4, 6, 8)
    print(f"Addition Result: {result}")

    # Subtraction
    result = math_ops.subtract(10, 3)
    print(f"Subtraction Result: {result}")

    result = math_ops.subtract(20, 5, 3)
    print(f"Subtraction Result: {result}")

    # Multiplication
    result = math_ops.multiply(2, 5)
    print(f"Multiplication Result: {result}")

    result = math_ops.multiply(3, 4, 2)
    print(f"Multiplication Result: {result}")

main()
