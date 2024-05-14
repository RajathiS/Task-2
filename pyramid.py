def pyramid(row):
    value = 1
    for i in range(1, row + 1):
        print(" " * (row - i), end="")
        for j in range(1, i + 1):
            print(value, end=" ")
            value += 1
            if value > 20:
                break
        print(" ")
pyramid(6)
