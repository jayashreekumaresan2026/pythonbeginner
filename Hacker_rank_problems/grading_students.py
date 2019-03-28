def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade > 37:
            reminder = grade % 5
            if reminder > 2:
                grade = grade + (5 - (grade % 5))
        final_grades.append(grade)

    return final_grades


array_grades = [73, 67, 38, 33]
print(gradingStudents(array_grades))
