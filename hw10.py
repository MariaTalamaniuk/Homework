def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Це не схоже на число. Будь ласка, спробуйте ще раз.")

def get_operation():
    operations = {'+': lambda x, y: x + y, # також можна використати if elif
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}
    while True:
        op = input("Введіть операцію (+, -, *, /): ")
        if op in operations:
            return operations[op]
        else:
            print("Невідома операція. Виберіть з перелічених: +, -, *, /.")

def main():
    print("Простий калькулятор")
    number1 = get_number("Введіть перше число: ")
    number2 = get_number("Введіть друге число: ")
    operation = get_operation()

    try:
        result = operation(number1, number2)
        print("Результат: ", result)
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль не допустиме.")

if __name__ == "__main__":
    main()
