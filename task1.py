"""
# Exercise 1 (Polymorphism - Negator):
Write a class called Negator
  use @singlesipatchmethod on the neg method
if you use int  as argument return the negative value of this integer
if you use bool  return the oppsite boolean
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

"""
# Solution

from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

    @neg.register
    def _(self, arg: str):
        return ""

# Usage
obj = Negator()
print(obj.neg(1))      # Output: -1
print(obj.neg(True))   # Output: False
print(obj.neg('Hello'))# Output: ''

print("_______________________________________")

from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

    @neg.register
    def _(self, arg: str):
        return ""

# Usage
obj = Negator()
print(obj.neg(1))        # Output: -1
print(obj.neg(True))     # Output: False
print(obj.neg('Hello'))  # Output: ''

