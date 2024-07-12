# У вас є два списки студентів, які зареєструвалися на два різні курси. Потрібно визначити:
# Студентів, які зареєструвалися на обидва курси.
# Студентів, які зареєструвалися лише на один з курсів.
# Студентів, які зареєструвалися хоча б на один з курсів.
# Студентів, які зареєструвалися тільки на перший курс.
# Студентів, які зареєструвалися тільки на другий курс.
students_course1 = set(["Anna", "Bohdan", "Clara", "Dmytro", "Elena"])
students_course2 = set(["Clara", "Elena", "Fedor", "George", "Hanna"])
# Вихідні дані:
# Студенти, які зареєструвалися на обидва курси.
# Студенти, які зареєструвалися лише на один з курсів.
# Студенти, які зареєструвалися хоча б на один з курсів.
# Студенти, які зареєструвалися тільки на перший курс.
# Студенти, які зареєструвалися тільки на другий курс.

all_students = students_course1 & students_course2
print(all_students)

students_from_one = students_course1 ^ students_course2
print(students_from_one)

students_from_both = students_course1 | students_course2
print(students_from_both)

print(students_course1)

print(students_course2)