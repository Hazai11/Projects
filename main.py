# Computer Architecture & Organization: 8-bit Binary Converter
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

byte_data = "10101000"
print(f"Binary: {byte_data} -> Decimal: {binary_to_decimal(byte_data)}")