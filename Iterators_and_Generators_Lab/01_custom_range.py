class custom_range:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= self.end:
            return self.counter

        raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
