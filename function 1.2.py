
def get_grade(subject="Unknown", marks=0):
    print("Subject:", subject)

    if marks<0 or marks>100:
        print("Invalide")

    elif marks <35:
        print("W")

    elif marks < 55:
        print("S")

    elif marks < 65:
        print("C")

    elif marks <75:
        print("B")

    else:
        print("A")

get_grade(marks = 56, subject="Maths")