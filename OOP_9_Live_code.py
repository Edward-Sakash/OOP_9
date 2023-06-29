# 1. Single Responsibility Principle (SRP) 

class Adder:
    def add(self, a, b):
        return a + b
    
class Subtractor:
    def subtract(self, a, b):
        return a - b


class Calculator:
    def __init__(self, adder, subtractor):
        self.adder = adder
        self.subtractor = subtractor

    def add(self, a, b):
        return self.adder.add(a, b)
    
    def subtract(self, a, b):
        return self.subtractor.subtract(a, b)


adder = Adder()
substractor = Subtractor()

calculate = Calculator(adder, substractor)

print(calculate.add(1,2))
print(calculate.subtract(1,2))

print("___________________________")

class PaymentProcess:
    def process_payment(self):
        # process credit card payment
        pass

    def process_paypal_payment(self):
          # process paypal payment
        pass

class PaymentProcessor:
    def process_payment(self):
       # process credit card payment
        pass

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self):
       # process paypal payment
        pass

# The Liskov Substitution Principle (LSP)

from abc import ABC, abstractclassmethod 

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return 'Rectangle'

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
    
    def __str__(self):
        return 'Square'

def print_area(shape):
    print(f"The area {shape} is: {shape.area()}")

rectangle = Rectangle(4,5)
square = Square(4)

#print_area(rectangle)
#print_area(square)


## Singleton Pattern
#Version 1

class School:
    class __School:
        def __init__(self, population):
            self.population = population

        def __str__(self):
            return f"School({self.population})"

        def add_students(self, number_of_std):
            self.population += number_of_std

    __instance = None

    def __new__(cls, population):
        # print(cls.__instance) #class variable of School
        # print(cls.__School)

        if cls.__instance == None:
            print('create instance only once')
            cls.__instance = cls.__School(population)
        return cls.__instance

obj1 = School(10)
obj2 = School(1000)
obj3 = School(1000)
# print(obj1 == obj2)
# print(id(obj1))
# print(id(obj2))


## Version 2


def singleton(class_):
    instance = {}


    def get_instance(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        print(instance)
        return instance[class_]
    return get_instance


@singleton
class FirstClass:
    def __init__(self, m):
        self.val = m

obj_first1 = FirstClass(12)
# obj_first2 = FirstClass(20)
# print(obj_first1.val)
# print(obj_first2.val)

@singleton
class SecondClass:
    def __init__(self):
        self.val = 0

    def __str__(self) -> str:
        return f'Second; value = {self.val}'


# print(obj_first1 == obj_first2)

obj_sec1 = SecondClass()
print(obj_sec1)
obj_sec1.val = 10
print(obj_sec1)
obj_sec2 = SecondClass()
print(obj_sec2)
         

