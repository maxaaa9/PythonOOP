def multiply(multi):  # decorator parameter
    def decorator(function):  # that define to function below
        def wrapper(num):  # this is the parameter which is given to the function
            return multi * function(num)
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
