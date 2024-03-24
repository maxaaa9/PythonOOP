def squares(number) -> list:
    for n in range(1, number + 1):
        yield n*n

print(list(squares(5)))