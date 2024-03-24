class vowels:

    def __init__(self, string: str):
        self.string = string
        self.vowels: str = "aeiuyo"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.string):
            if self.string[self.index].lower() in self.vowels:
                return self.string[self.index]
            return self.__next__()
        raise StopIteration


my_string = vowels('AAEEOOIUYO')
for char in my_string:
    print(char)