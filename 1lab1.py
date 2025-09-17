import math

print("Расчёт площади треугольника по формуле Герона")
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

p = (a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Площадь треугольника: {area:.2f}")
