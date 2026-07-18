from functools import wraps
def my_decorator(func):

    # @wraps(func)
    def wrapper():

        print("This top of the wrapper")
        func()
        print("This bottom of the wrapper")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorator class")

#this acually means 
# def greet():
#     print("Hello from decorator class")

# greet = my_decorator(greet)
# So greet is replaced by whatever my_decorator() returns.


greet()
print(greet.__name__)

#summary 
# A decorator is a function that takes another function,
# adds extra behavior before or after it, and returns the modified function. 
# The @decorator syntax is just shorthand for func = decorator(func), and 
# @wraps preserves the original function's metadata like its name and docstring.