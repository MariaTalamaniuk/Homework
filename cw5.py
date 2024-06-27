Elon_Musk = {
    'name': 'Elon',
    'age': 56,
    'second_name': 'Musk'
}

Kylie_Jenners = {
    'name': 'Kylie',
    'age': 32,
    'second_name': 'Jenners'
}

celebrity_name = input('Введіть імʼя знаменитості: ')

if celebrity_name == 'Ілон Маск':
    for key, value in Elon_Musk.items():
        print(f'{key} : {value}')

elif celebrity_name == 'Кайлі Дженерс':
    for key, value in Kylie_Jenners.items():
        print(f'{key}: {value}')