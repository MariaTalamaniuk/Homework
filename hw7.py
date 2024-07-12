# Напишіть функцію, яка приймає два списки чисел і виконує такі операції:
#
#  1. Об’єднання множин.
#  2. Перетин множин.
#  3. Різницю першої множини від другої.
#  4. Перевіряє, чи є перший список підмножиною другого.

short_fur = set(['Bengal', 'British', 'Siamese', 'Bombay', 'Maine Coon'])
long_fur = set(['Persian', 'Siberian', 'Maine Coon', 'Himalayan', 'Siamese'])

all_fur = short_fur | long_fur
print(all_fur)

intersection_fur = short_fur & long_fur
print(intersection_fur)

difference_fur = short_fur ^ long_fur
print(difference_fur)

check_fur = short_fur.issubset(long_fur)
print(check_fur)