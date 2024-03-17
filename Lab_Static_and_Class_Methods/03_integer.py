class Integer:
    ROMAN_DICT = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_int = 0

        for i in range(len(value)):
            if i != 0 and cls.ROMAN_DICT[value[i]] > cls.ROMAN_DICT[value[i - 1]]:
                roman_int += cls.ROMAN_DICT[value[i]] - 2 * cls.ROMAN_DICT[value[i - 1]]
            else:
                roman_int += cls.ROMAN_DICT[value[i]]

        return cls(roman_int)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))