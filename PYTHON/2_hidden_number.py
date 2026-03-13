import random
import os
#gusse hidden number
def game():
    if os.path.exists("score.txt"):
      with open("score.txt","r") as f:
        score = int(f.read())
    else:
       score=0
    
    hidden = random.randint(1,50)
    print("welcome to hidden guessing game")
    print("guess between 1 to 50")
    print("you will get 3 chance.\neach win get 10 points")
    for i in range(1,8):
        guess = int(input(f"Chance{i}-enter any number between(1,50):"))
        if(guess>hidden):print("Too big number!")
        elif(guess<hidden):print("Too small number!")
        if(guess==hidden):
            print("you won get 10 scores!\n hidden number is ",hidden)
            score=score+10
            break
        else:
            print(f"wrong guess!!")
    print(f"your highest total score is {score}")
    with open("score.txt","w") as f:
                f.write(str(score))
game()
