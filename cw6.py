import random

numbers = tuple(random.randint(1,100) for _ in range(10))
print(numbers)

max_num = numbers[0]
min_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number
    if number < max_num:
        min_num = number

print(f'max number: {max_num}\nmin number: {min_num}')


numberies = []

for i in numbers:
    if i % 2 == 0:
        numberies.append(i)

print(numberies)

sum_numbers = 0

for i in numbers:
    sum_numbers += i
print(sum_numbers)

ar_numbers = sum_numbers % len(numbers)

print(ar_numbers)