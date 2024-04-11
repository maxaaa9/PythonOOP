def even_numbers(function):
    def wrapper(number):
        data = number
        return list(num for num in data if num % 2 == 0)
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))

