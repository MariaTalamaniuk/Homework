def check_parity():
    try:
        # Запит на введення числа
        number = int(input("Будь ласка, введіть число: "))

        # Перевірка на парність числа
        if number % 2 == 0:
            print("Число парне.")
        else:
            print("Число непарне.")
    except ValueError:
        print("Це не валідне число. Будь ласка, спробуйте ще раз.")
check_parity()  # Рекурсивний виклик функції


# Виклик функції
check_parity()
