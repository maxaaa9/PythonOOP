def rhombus(size):
    my_string = ""
    for top in range(1, size + 1):
        my_string += f"{' ' * (size - top)}{'* ' * top}\n"
    for bot in range(size - 1, 0, -1):
        my_string += f"{' ' * (size - bot)}{'* ' * bot}\n"

    return my_string


rhombus_size = int(input())
print(rhombus(rhombus_size))
