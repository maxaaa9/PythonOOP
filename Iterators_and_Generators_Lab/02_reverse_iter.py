class reverse_iter:

    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.counter = len(self.iter_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter -= 1
        if self.counter >= 0:
            return self.iter_list[self.counter]

        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
