for i in range(10000):
    # Convert the integer to a 4-digit string
    combination = str(i).zfill(4)

    # Check if all characters are digits and in the range 0-9
    if all(c.isdigit() and 0 <= int(c) <= 9 for c in combination):
        print(combination)