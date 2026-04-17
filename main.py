def average_grades(d):
    result = {}
    for student, subjects in d.items():
        avg = sum(subjects.values()) / len(subjects)
        result[student] = round(avg, 1)
    return result

def top_student(d):
    averages = average_grades(d)
    return max(averages, key=averages.get)

students = {
    'Ali': {'math': 85, 'science': 90},
    'Vali': {'math': 78, 'science': 82}
}
print(average_grades(students))   # {'Ali': 87.5, 'Vali': 80.0}
print(top_student(students))      # Ali
