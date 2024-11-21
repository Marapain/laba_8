# Автор: Клепач_Костянтин

# Словник для зберігання інформації про успішність студентів
students_performance = {
    "КН-35": [  # Номер групи
        {
            "name": "Клепач Костянтин Костянтинович",  # Прізвище, ім'я, по батькові
            "course": 2,  # Курс
            "subjects": {  # Предмети та оцінки
                "Організація ІТ-бізнесу": [5, 4, 5],
                "Чисельні методи": [4, 4, 5],
                "Обслуговування комп'ютерної техніки": [5, 5, 5],
            },
        },
        {
            "name": "Петренко Петро Петрович",
            "course": 2,
            "subjects": {
                "Організація ІТ-бізнесу": [3, 4, 4],
                "Чисельні методи": [4, 3, 4],
                "Обслуговування комп'ютерної техніки": [5, 4, 4],
            },
        },
    ]
}

# Функція для додавання студента в словник
def add_student(group_number, name, course, subjects):
    """
    Додає нового студента до групи.
    :param group_number: Номер групи
    :param name: ПІБ студента
    :param course: Курс студента
    :param subjects: Предмети та оцінки
    """
    if group_number not in students_performance:
        students_performance[group_number] = []

    students_performance[group_number].append({
        "name": name,
        "course": course,
        "subjects": subjects,
    })

# Демонстрація додавання нового студента
add_student(
    "101",
    "Сидоренко Марія Іванівна",
    2,
    {"Організація ІТ-бізнесу": [5, 5, 5], "Чисельні методи": [5, 4, 5], "Обслуговування комп'ютерної техніки": [5, 5, 5]},
)

# Вивід словника
for group, students in students_performance.items():
    print(f"Група: {group}")
    for student in students:
        print(f"  {student['name']}, курс {student['course']}, оцінки: {student['subjects']}")