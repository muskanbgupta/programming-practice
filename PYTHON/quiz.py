# Quize game
score=0
Questions= ("1. What does 'OOP' stand for in programming?",
          "2.Which data structure uses FIFO (First In, First Out)?",
          "3. What is the purpose of a loop in programming?",
          "4.Which language is primarily used for web page structure?")

options=(("A) Object-Oriented Process","B) Object-Oriented Programming","C) Operational Object Program","D) Organized Output Process"),
         ("A) Stack","B) Queue ","C) Tree" ,"D) Graph"),
         ("A) To store data","B) To execute a block of code repeatedly","C) To define variables","D) To compile code"),
         ("A) Python","B) C++","C) HTML","D) Java"))

Answers=("B","B","B","C")
user="yes"
print("----Quize game----")
while user=="yes" or "y":

        for Q in range(len(Questions)):
                print(Questions[Q])
                for o in options[Q]:
                        print(o)
                opinion=input("Enter your Option:").upper()
                if opinion==Answers[Q]:
                        print("\nYour Answer is correct ✔️\n")
                        score+=1
                else:
                        print(f"\nYour Answer is Wrong ❌ \nCorrect Option is {Answers[Q]}\n")
        print()
        print(f"Total score :{score}/4 ")
        user=input(f"do you want u play again?(yes/Y):").lower()
        if user=="yes":
                score=0
        