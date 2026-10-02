def add_hex(h1, h2):
    total = int(h1, 16) + int(h2, 16)
    return hex(total)

def subtract_hex(h1, h2):
    difference = int(h1, 16) - int(h2, 16)
    return hex(difference)

user_hex1 = input("Enter first hexadecimal number: ")
user_hex2 = input("Enter second hexadecimal number: ")

print("Sum:", add_hex(user_hex1, user_hex2))
print("Difference:", subtract_hex(user_hex1, user_hex2))

def add_binary(b1, b2):
    total = int(b1, 2) + int(b2, 2)
    return bin(total)

def subtract_binary(b1,b2):
    difference = int(b1, 2) - int(b2, 2)
    return bin(difference)

user_binary1 = input("Enter first binary number: ")
user_binary2 = input("Enter second binary number: ")

print("Sum:", add_binary(user_binary1, user_binary2))
print("Difference:", subtract_binary(user_binary1, user_binary2))

def add_decimal(d1, d2):
    total = int(d1) + int(d2)
    return total
def subtract_decimal(d1, d2):
    difference = int(d1) - int(d2)
    return difference

user_decimal1 = input("Enter first decimal number: ")
user_decimal2 = input("Enter second decimal number: ")

print("Sum:", add_decimal(user_decimal1, user_decimal2))
print("Difference:", subtract_decimal(user_decimal1, user_decimal2))