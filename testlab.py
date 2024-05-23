def calculate_average_grades(data):
    total_math = 0
    total_cs = 0

    num_students = len(data)

    for record in data:
        total_math += record['math']
        total_cs += record['cs']

    average_math = total_math / num_students
    average_cs = total_cs / num_students

    average_grades = {'math': average_math, 'cs': average_cs}

    return average_grades



data = [
    {'id': 1, 'math': 76.0, 'cs': 81.0},
    {'id': 2, 'math': 73.5, 'cs': 78.5},
    {'id': 3, 'math': 80.5, 'cs': 85.5}
]

print(calculate_average_grades(data))