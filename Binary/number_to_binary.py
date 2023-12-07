number = int(input("input your number: "))


def number_to_binery(decimal):
    binary = ""

    if decimal == 0:
        binary = "0"
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    return binary


binary_output = number_to_binery(number)

print("binary: ", binary_output)
