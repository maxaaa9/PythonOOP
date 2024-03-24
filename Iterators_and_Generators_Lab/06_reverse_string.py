# def reverse_text(my_string: str):
#     """This function is better for readability"""
#     for s in my_string[::-1]:
#         yield s

def reverse_text(my_string: str):
    """This function is better for control and memory efficiency,
     because its not not created reserved copy, like slicing"""
    current_index = -1
    while current_index >= -len(my_string):
        yield my_string[current_index]
        current_index -= 1


for char in reverse_text("step"):
    print(char, end='')