def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def decimal_to_octal(n):
    if n == 0:
        return ""
    else:
        return decimal_to_octal(n // 8) + str(n % 8)

decimal_number = int(input("Введите десятичное число: "))

binary_representation = decimal_to_binary(decimal_number) or "0"
octal_representation = decimal_to_octal(decimal_number) or "0"

print(f"Двоичное представление: {binary_representation}")
print(f"Восьмеричное представление: {octal_representation}")
