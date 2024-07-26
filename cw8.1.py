def distribute(age):
    if age < 18:
        return f'Ваш вік: {age} - вік дитини.'
    elif 18 <= age < 21:
        return f'Ваш вік: {age} - вік підлітка.'
    else:
        return f'Ваш вік: {age} - вік дорослого.'

print(distribute(19))