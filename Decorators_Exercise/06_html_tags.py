def tags(decorator_param):
    def decorator(func):
        def wrapper(*args):
            return f"<{decorator_param}>{func(*args)}</{decorator_param}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
