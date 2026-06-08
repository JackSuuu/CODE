def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# say_hello()

# print("==========================================================")

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
                print(kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(**kwargs):
    print(kwargs)

# greet(name="World")