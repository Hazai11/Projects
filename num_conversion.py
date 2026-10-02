def to_decimal(binary_str):
    return int(binary_str, 2)
def to_octal(binary_str):
    return oct(int(binary_str, 2))
def to_hexadecimal(binary_str):
    return hex(int(binary_str, 2))

user_binary= input("Enter a binary num: ")
print("Decimal", to_decimal(user_binary))
print("Octal", to_octal(user_binary))
print("Hexadecimal", to_hexadecimal(user_binary))