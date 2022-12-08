#3 задание
import math
a, b, c = map(float, input("Введите коэффициенты для квадратного уравнения (a, b, c): ").split())
d = (b ** 2) - 4 * (a * c)
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Ответ: {x1, x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"Ответ: {-b/2*a}")
else:
    print("Корней нет")