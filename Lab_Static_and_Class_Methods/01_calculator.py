from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        result = sum(args)
        return result

    @staticmethod
    def multiply(*args):
        result = reduce(lambda a, b: a * b, args)
        return result

    @staticmethod
    def divide(*args):
        result = reduce(lambda a, b: a / b, args)
        return result

    @staticmethod
    def subtract(*args):
        result = reduce(lambda a, b: a - b, args)
        return result