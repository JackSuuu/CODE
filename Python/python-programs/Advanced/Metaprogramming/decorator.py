"""
Here, @my_decorator modifies the behavior of say_hello without changing its code 
— this is a form of metaprogramming (code that manipulates code).
"""

def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
