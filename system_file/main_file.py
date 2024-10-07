import os

# Файл для зберігання завдань
FILENAME = 'tasks.txt'

# Функція для додавання нового завдання
def add_task():
    task = input("Введіть опис завдання: ")
    with open(FILENAME, 'a') as file:
        file.write(f"[ ] {task}\n")
    print("Завдання додано!")

# Функція для показу всіх завдань
def show_tasks():
    if not os.path.exists(FILENAME):
        print("Немає завдань.")
        return []
    with open(FILENAME, 'r') as file:
        tasks = file.readlines()
    if tasks:
        print("Ваші завдання:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task.strip()}")
        return tasks
    else:
        print("Немає завдань.")
        return []

# Функція для видалення завдання
def delete_task():
    tasks = show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введіть номер завдання для видалення: "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            with open(FILENAME, 'w') as file:
                file.writelines(tasks)
            print("Завдання видалено!")
        else:
            print("Неправильний номер завдання.")
    except ValueError:
        print("Введіть коректний номер.")

# Функція для редагування завдання
def edit_task():
    tasks = show_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Введіть номер завдання для редагування: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Введіть новий текст завдання: ")
            tasks[task_num - 1] = f"[ ] {new_task}\n"
            with open(FILENAME, 'w') as file:
                file.writelines(tasks)
            print("Завдання оновлено!")
        else:
            print("Неправильний номер завдання.")
    except ValueError:
        print("Введіть коректний номер.")

# Основна функція для вибору дій
def main():
    while True:
        print("\nМеню:")
        print("1. Додати завдання")
        print("2. Показати завдання")
        print("3. Видалити завдання")
        print("4. Редагувати завдання")
        print("5. Вийти")
        choice = input("Виберіть дію: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == '__main__':
    main()