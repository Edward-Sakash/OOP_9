"""
Exercise 3 - Singleon Pattern (Version 3):
Complete the following code:

class Singleton:
    _instances = {}

    def __init__(self, class_):
        self._class = class_
        # self._instances = {}

    def __call__(self, *args, **kwargs):
        if self._class not in self._____:
            self._instances[_______] = _________________
        return self._instances[self._______]

@Singleton
class FirstClass:
    def __init__(self, m):
        self.val = m

a = FirstClass(1)
b = FirstClass(23)

a == b #True

research the __ call__ method
fill out the _______ spaces.
make sure that only one instance per class is created

"""

# Solution 1
# with using class decorator

class Singleton:
    _instances = {}  # Dictionary to store the instances of decorated classes

    def __init__(self, class_):
        self._class = class_  # The class being decorated

    def __call__(self, *args, **kwargs):
        if self._class not in self._instances:  # Check if class instance already exists
            # Create a new instance of the class and store it in the dictionary
            self._instances[self._class] = self._class(*args, **kwargs)
        return self._instances[self._class]  # Return the instance from the dictionary

@Singleton
class FirstClass:
    def __init__(self, m):
        self.val = m

a = FirstClass(1)
b = FirstClass(23)

print(a == b)  # True (Both variables reference the same instance)

print("_____________________________________________")

# Solution 2
# using metaclasses to implement the Singleton pattern

class SingletonMeta(type):
    _instances = {}  # Dictionary to store the instances of classes

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:  # Check if class instance already exists
            # Create a new instance of the class using the metaclass's __call__ method
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]  # Return the instance from the dictionary

class FirstClass(metaclass=SingletonMeta):
    def __init__(self, m):
        self.val = m

a = FirstClass(1)
b = FirstClass(23)

print(a == b)  # True (Both variables reference the same instance)

print("_____________________________________________")

# Solution 3
# with using function decorator

def singleton(class_):
    instances = {}  # Dictionary to store the instances of classes

    def wrapper(*args, **kwargs):
        if class_ not in instances:  # Check if class instance already exists
            # Create a new instance of the class using the provided class and arguments
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]  # Return the instance from the dictionary

    return wrapper

@singleton
class FirstClass:
    def __init__(self, m):
        self.val = m

# Create instances of FirstClass
a = FirstClass(1)
b = FirstClass(23)

# Check if a and b refer to the same instance
print(a == b)  # True (Both variables reference the same instance)

print("__________________________________________________")

# Solution 4
# with using Factory Pattern

class FirstClass:
    def __init__(self, m):
        self.val = m

class SecondClass:
    def __init__(self, m):
        self.val = m

class SingletonFactory:
    _instances = {}  # Dictionary to store the instances of each class

    @classmethod
    def create_instance(cls, class_name, *args, **kwargs):
        if class_name not in cls._instances:  # Check if instance already exists
            # Create a new instance of the specified class and store it in the dictionary
            cls._instances[class_name] = class_name(*args, **kwargs)
        return cls._instances[class_name]  # Return the instance

# Create instances using the SingletonFactory
factory = SingletonFactory()
a = factory.create_instance(FirstClass, 1)  # Create an instance of FirstClass
b = factory.create_instance(FirstClass, 23)  # Create another instance of FirstClass

print(a == b)  # True, both a and b refer to the same instance of FirstClass


