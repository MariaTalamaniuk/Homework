#вирішити просту задачу mass
#2.0) знайти додати до кожного масива число 8
#2.1) знайти  cos кожного числа
#2.2) Знайти суму всіх чисел

import math

mass = [[1,2,3,4,5,6],[8,5,2,7,3,1]]

for sublist in mass:
    sublist.append(8)

print(mass)

mass_cos = [[math.cos(x) for x in sublist] for sublist in mass]

print(f'\n{mass_cos}')

total_sum = sum(sum(sublist) for sublist in mass)

print(f'\n{total_sum}')

