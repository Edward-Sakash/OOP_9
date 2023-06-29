"""
 Exercise 4 (Singleton Logger):

Implement a Singleton class called Logger that keeps track of logs generated by different parts of a system. The Logger class should have the following behavior:
It should maintain a list of log messages.
 It should provide a method called add_log that takes a message as input and adds it to the list of logs.
It should provide a method called get_logs that returns the list of logs.
Your task is to implement the Logger class as a Singleton, ensuring that only one instance of the class can exist.
Hint: You can use the singleton decorator from today's class.

class Logger:
.........
.........

# Testing the Singleton Logger
logger1 = Logger()
logger1.add_log("Log message 1")

logger2 = Logger()
logger2.add_log("Log message 2")

logger3 = Logger()
logger3.add_log("Log message 3")

# All instances of the logger will have the same logs
print(logger1.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger2.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger3.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']

"""

# Solution 1
# Decorator-based Singleton

def singleton(class_):
    instances = {}  # Dictionary to store the instances of classes

    def wrapper(*args, **kwargs):
        if class_ not in instances:  # Check if class instance already exists
            instances[class_] = class_(*args, **kwargs)  # Create a new instance of the class and store it in the dictionary
        return instances[class_]  # Return the instance from the dictionary

    return wrapper


@singleton
class Logger:
    def __init__(self):
        self.logs = []  # List to store the log messages

    def add_log(self, message):
        self.logs.append(message)  # Add the log message to the list of logs

    def get_logs(self):
        return self.logs  # Return the list of logs


# Testing the Singleton Logger
logger1 = Logger()
logger1.add_log("Log message 1")

logger2 = Logger()
logger2.add_log("Log message 2")

logger3 = Logger()
logger3.add_log("Log message 3")

# All instances of the logger will have the same logs
print(logger1.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger2.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger3.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']

print("________________________________")

# Solution 2
# an alternative solution to implement the Singleton Logger using a class-level attribute:

class Logger:
    _instance = None  # Class-level attribute to store the single instance of the Logger
    logs = []  # Class-level attribute to store the logs

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Check if the instance has already been created
            cls._instance = super().__new__(cls, *args, **kwargs)  # Create a new instance if it doesn't exist
        return cls._instance  # Return the single instance of the Logger

    def add_log(self, message):
        self.logs.append(message)  # Add the log message to the list of logs

    def get_logs(self):
        return self.logs  # Return the list of logs


# Testing the Singleton Logger
logger1 = Logger()
logger1.add_log("Log message 1")

logger2 = Logger()
logger2.add_log("Log message 2")

logger3 = Logger()
logger3.add_log("Log message 3")

# All instances of the logger will have the same logs
print(logger1.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger2.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
print(logger3.get_logs())  # Output: ['Log message 1', 'Log message 2', 'Log message 3']
