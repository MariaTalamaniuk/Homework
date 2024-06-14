# 12. Створити словник з інформацією про ресторан (назва, адреса, тип кухні) і вивести всі пари ключ-значення.

restaurant = {
    'name': 'Nightfall',
    'address': 'France, Paris, Champs-élysées',
    'cuisine type': 'french',
}

print(restaurant.keys())

# 22. Перевірити, чи існує певний ключ у словнику (наприклад, "ціна") і вивести відповідне значення.

key = input('Enter the key you wish to find: ')

if key in restaurant:
    print(f"\nThe value for '{key}': {restaurant[key]}")
else:
    print(f"\nThe value '{key}' is not found.")

# 25. Створити словник, що містить дні тижня та їх порядкові номери. Вивести порядковий номер середи.

days_of_the_week = {
    'sunday': 1,
    'monday': 2,
    'tuesday': 3,
    'wednesday': 4,
    'thursday': 5,
    'friday': 6,
    'saturday': 7
}

wednesday_num = days_of_the_week['wednesday']
print(f'\nWednesday sequence number:, {wednesday_num}\n')

# 26. Створити словник з інформацією про страву (назва, інгредієнти, час приготування) і вивести всі пари ключ-значення.

dishes_names = {
    'name': 'omelette',
    'ingredients': 'an egg, pepper, salt',
    'cooking time': '5 mins'
}

for key, value in dishes_names.items():
    print(f"Key: {key}, Value: {value}")x