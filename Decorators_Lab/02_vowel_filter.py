def vowel_filter(numbers):
    def wrapper():
        result = numbers()
        return [vow for vow in result if vow.lower() in "aeiyuo"]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "a", "b", "c", "d", "e"]

print(get_letters())