def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Викликаємо функцію множення: {func.__name__}')
        print(f'Ваші аргумнти: {args}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Ваш результат: {result}\n')
        return result
    return wrapper

# юзаємо декоратор та створюємо функцію множення
@log_decorator
def multiply(a, b):
    return a * b

# перевірка фунції
multiply(3, 5)
multiply(a=7, b=2)
multiply(0, 100)