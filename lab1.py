import numpy as np

z1 = np.random.randint(0, 10, 10)
z2 = np.random.randint(0, 10, 10)

# Находим одинаковые элементы
common_elements = np.intersect1d(z1, z2)

print("Первый массив:", z1)
print("Второй массив:", z2)
print("Одинаковые элементы:", common_elements)