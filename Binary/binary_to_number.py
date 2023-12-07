def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for bit in binary:
        decimal += int(bit) * (2 ** power)
        power -= 1

    return decimal

binary_number = "13"
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)