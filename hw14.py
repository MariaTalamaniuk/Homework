def limit_calls(max_calls):
    def decorator(func):
        calls = 0


        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print(f"Функцію {func.__name__} більше викликати не можна.")

        return wrapper

    return decorator


@limit_calls(max_calls=3)
def greet(name):
    return f"Привіт, {name}!"


print(greet("Сергій"))
print(greet("Марія"))
print(greet("Олег"))
print(greet("Анна"))
print(greet("Катерина"))


# в 17 рядку можна змінювати максимальну кількість викликів функції (max_calls=3)