
def get_grade(*marks):
    print(type(marks))
    total = 0
    for i in marks:
        total+= i
    
    print(total)

get_grade(80, 55, 60)