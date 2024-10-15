def solve_equation(a, b, c):
    return a * b + 4 * c

# Ввод значений с клавиатуры
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

# Вычисление x
x = solve_equation(a, b, c)

# Вывод результата
print("Результат уравнения x = a * b + 4 * c:", x)
