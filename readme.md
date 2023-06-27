# Exercise 1 (Polymorphism - Negator):
Write a class called Negator
  use @singlesipatchmethod on the neg method
if you use int  as argument return the negative value of this integer
if you use bool  return the opposite boolean
if you use str return an empty string
class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")
......
......
......
obj = Negator()
obj.neg(1) #--> -1
obj.neg(True) #--> False
obj.neg('Hello') #--> ''

# Exercise 2 (Polymorphism - OverloadingII- Math):
- Create a Python class called MathOperations with overloaded methods for:
1. addition (add()),
2. subtraction (subtract()), and
3. multiplication (multiply()).
Each method should take different numbers of arguments and perform the corresponding operation.
In your main() function, create an instance of the MathOperations class and demonstrate the polymorphic behavior by calling each method with different numbers of arguments.

class MathOperations:
    def add(...):
....
....

    def subtract(....):
....
....

    def multiply(....):
....
....

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