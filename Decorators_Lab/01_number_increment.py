def number_increment(num):
    def increase():
        return [el+1 for el in num]

    return increase()

print(number_increment([1, 2, 3]))