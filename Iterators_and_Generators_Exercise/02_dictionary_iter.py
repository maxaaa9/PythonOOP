class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.len_of_dict = len(self.dictionary) - 1
        self.counter = -1
    @property
    def dictionary(self):
        return self.__dictionary

    @dictionary.setter
    def dictionary(self, value):
        try:
            self.__dictionary = tuple(value.items())
        except Exception:
            raise Exception("Wrong data!")

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.len_of_dict:
            raise StopIteration

        self.counter += 1
        return self.__dictionary[self.counter]