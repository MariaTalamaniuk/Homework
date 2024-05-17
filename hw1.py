# порівняти 3 числа і вивести  найбільше

print('Задайте 3 цілі числа. ')

number1 = input('Задайте 1 число: ')
number2 = input('Задайте 2 число: ')
number3 = input('Задайте 3 число: ')

max_number = number1

if number1 > max_number:
    max_number = number2
if number3 > max_number:
    max_number = number3
print(f'Найбільше число: {max_number}')
