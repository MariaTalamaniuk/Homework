mass = [[1,2,3],[5,6,7]]
mass[0].append(4)
sum = 0
for i in mass:
    for j in i:
        sum += j
print(sum)