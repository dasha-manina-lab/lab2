units = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.34,
    "yd": 0.9144
}

print("Доступные единицы: km, m, cm, mm, mi, yd")
source_unit = input("Выберите исходную единицу измерения: ")
target_unit = input("Выберите целевую единицу измерения: ")
value = float(input("Введите значение: "))

meters = value * units[source_unit]
result = meters / units[target_unit]

print(f"{value} {source_unit} = {result:.4f} {target_unit}")
