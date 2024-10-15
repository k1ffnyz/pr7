def to_ternary(n):
    if n == 0:
        return ''
    else:
        return to_ternary(n // 3) + str(n % 3)


decimal_number = int(input("Введите десятичное число: "))
if decimal_number == 0:
    print("Троичное представление: 0")
else:
    ternary_representation = to_ternary(decimal_number)
    print("Троичное представление:", ternary_representation)
