def halfTriangle(rows):
    for x in range(0, rows):
        for y in range(0, x + 1):
            print("*", end = ' ')

        print("\n")

# Excution
halfTriangle(6)