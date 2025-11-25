#list of questions
#store the answers
#randomly pick questions
#ask the questions
#see if they are correct
#keep track of the score
#tell the user their score

import random

questions = {
"What is Python?" :"Python is a high-level, interpreted programming language",



"What are the basic data types in Python?":"The basic data types are int, float, str, and bool",

"What is an integer (int)?":"An integer is a whole number like 5, −2, or 100",

"What is a float?":"A float is a number with decimals like 3.14 or 2.05",

"What is the output of print(3 + 2)?":"5",

"What is the output of print(10 / 2)?":"5.0",

"What is the output of print(7 % 3)?":"1",

"What is a list?":"A list is an ordered and changeable collection of items",

"What is a loop?":"A loop repeats a block of code multiple times",

"What is the output of the following code: print(4 * 3)?" :"12"

}

#key = questions, value = answers

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    for idx,question in enumerate(selected_questions):
        print(f"Question {idx + 1}.{question}")
        user_answer = input("your answer:").lower().strip()

        correct_answer = questions[question].lower().strip() 

        if user_answer == correct_answer.lower().strip():
            print("Correct!\n")
            score += 1

        else:
            print(f"wrong! correct answer is : {correct_answer}\n")

    print(f"your final score is : {score}/{total_questions}")


python_trivia_game()
   