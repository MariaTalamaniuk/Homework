print('Задайте 3 цілі числа. ')

number1 = int(input('Задайте 1 число: '))
number2 = int(input('Задайте 2 число: '))
number3 = int(input('Задайте 3 число: '))

max_number = number1  # Призначаємо перше число як початкове максимальне

if number2 > max_number:
    max_number = number2
if number3 > max_number:
    max_number = number3

print(f'Найбільше число: {max_number}')
