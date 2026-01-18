def get_grade(subject, marks):
    print("Subject: ", subject)

    if marks >= 75 and marks <= 100:
        grade = "A"
        print("grade: ", grade)
    elif marks >= 65 and marks < 75:
        grade = "B"
        print("grade: ", grade)
    elif marks >= 50 and marks < 65:
        grade = "C"
        print("grade: ", grade)
    elif marks >= 35 and marks < 50:
        grade = "S"
        print("grade: ", grade)
    else:
        print("grade: ", "F")

get_grade("Maths", 80)
get_grade("Science", 55)
    
    