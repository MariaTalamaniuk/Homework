import math
mass = [[1,2,3,4,5,6],[8,5,2,7,3,1]]

sin_mass = []

for i in mass:
    sin_i = []
    for j in i:
        sin_i.append(math.sin(j))
    sin_mass.append(sin_i)
print('Массив синусів:')
for row in sin_mass:
    print(row)

sum_in_mass = 0
for row in sin_mass:
    row_sum = sum(row)
    sum_in_mass += row_sum
print(sum_in_mass)