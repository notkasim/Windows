#problem2.4 (!!!Klar)
import random
def multi ():
    table = int(input("What multiplication table would you like to practice? "))
    questions = int(input("How many questions do want me to ask you? "))

    for numbers in range(questions):
        num = random.randint(1,12)
        user_question = f"{table} x {num} =?"
        correct_answer = table * num
        print(user_question)
        input_user = int(input("Write the answer: "))
        
        if input_user == correct_answer:
            print(f"Your answer is correct")
        else:
            print(f"The correct answer is {correct_answer}")
multi ()