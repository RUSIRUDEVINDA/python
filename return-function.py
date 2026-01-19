def get_grade(marks, subject=None):
    if marks < 0 or marks > 100:
        grade = "Invalid"
    elif marks < 35:
        grade = "W"
    elif marks < 55:
        grade = "S"
    elif marks < 65:
        grade = "C"
    elif marks < 75:
        grade = "B"
    else:
        grade = "A"

    print("Hello")

    return grade , subject

grade = get_grade(78, "Maths")
print(type(grade), grade)

if grade: # checking if grade is not None or not False
    print("Grade ", grade)
else:
    print("something went wrong")