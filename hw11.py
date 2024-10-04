def calculate_average(*grades, weight=1.0, bonus=0):
    if not grades:
        return 0
    weighted_average = sum(grade * weight for grade in grades) / len(grades)
    return weighted_average + bonus


result = calculate_average(85, 90, 78, weight=1.2, bonus=5)
print(f"Середня оцінка: {result}")
