# 1) Створює кортеж із 20 випадкових цілих чисел від 50 до 150.
# 2) Знаходить і виводить на екран всі числа, які є кратними 5.
# 3) Обчислює і виводить на екран кількість чисел, які менше середнього значення всіх чисел у кортежі.
# 4) Виводить на екран індекс першого входження числа 100 (або повідомлення, що такого числа немає).

import random
#1

numbers = tuple(random.randint(50,150) for _ in range(20))
print(numbers)

#2

numbers_divided_by_5 = []

for i in numbers:
    if i % 5 == 0:
        numbers_divided_by_5.append(i)

print(numbers_divided_by_5)

#3

average = sum(numbers_divided_by_5) / len(numbers_divided_by_5) if numbers_divided_by_5 else 0

less_than_average = sum(1 for i in numbers_divided_by_5 if i < average)

print(f"Середнє значення чисел кратних 5: {average}")
print(f"Кількість чисел кратних 5 і менших за середнє: {less_than_average}")

#4

if 100 in numbers:
    index = numbers.index(100)
    print(f"Індекс першого входження числа 100: {index}")
else:
    print("Число 100 у списку відсутнє.")