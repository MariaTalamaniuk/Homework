# Домашня робота
# 1) Створити програму, яка:
# 2) Зчитає введений користувачем рядок.
# 3) Виведе довжину цього рядка.
# 4) Виведе перший і останній символи рядка.
# 5) Виведе підрядок з другого по четвертий символи включно.
# 6) Перетворить всі символи рядка на великі.
# 7) Знайде позицію певного підрядка (наприклад, "світ") у введеному рядку.
# 8)Замінить усі пробіли на знак підкреслення (_).
# 9) Виведе отримані результати.
print("Enter any text or value: ")
text = input()
length = len(text)
print(length)

charArray = list(text)
print(charArray)

first_char = text[0]
last_char = text[-1]
print("First character:", first_char)
print("Last character:", last_char)
substring = text[1:4]
print("Substring from second to fourth characters:", substring)

print(text.upper())

text_with_underscores = text.replace(' ', '_')
print("Text with spaces replaced by underscores:", text_with_underscores)

print("Enter the substring to find its position: ")
search_substring = input()
position = text.find(search_substring)

if position != -1:
    print(f"The substring '{search_substring}' is found at position: {position}")
else:
    print(f"The substring '{search_substring}' is not found in the text.")
