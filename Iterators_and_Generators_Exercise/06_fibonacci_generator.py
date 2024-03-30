def fibonacci():
    num1 = 0
    num2 = 1

    while True:
        yield num1
        old_num1 = num1
        num1 = num2
        num2 += old_num1


generator = fibonacci()
for i in range(5):
    print(next(generator))

