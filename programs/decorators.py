def upper_decorator(func):
    def function_wrapper(string1):
        return string1.upper()
    return function_wrapper

@upper_decorator
def hello(string1):
    return string1

print(hello('goal'))

def upper_decorator(func):
    def function_wrapper(number):
        return number.count('5')
    return function_wrapper

@upper_decorator
def counter(number):
    return number

print(counter('564515'))