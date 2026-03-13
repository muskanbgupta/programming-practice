import random
#make random choice from computer
play_on="yes"
while(play_on=="yes"):
    computer = random.choice(("rock","paper","scissor"))
    print("----WELCOME TO THE GAME----")
    print("The Game is Rock,Paper and Scissors!")
    youstr = input("Enter your Choice:")
    youstr=youstr.lower()
    if(youstr=="scissors"):
            youstr="scissor"
    while youstr not in("rock","paper","scissor"):
        youstr=input("Please Enter Rock,Paper and Scissor!:").lower()
        
    print(f"YOU CHOOSE:{youstr}\nOPPONENT CHOOSE:{computer}")
    if(computer==youstr):
        print("draw!")
    else:
        if(computer=="rock" and youstr=="paper"):
            print("you win!")

        elif(computer=="paper" and youstr=="rock"):
                print("you lose!")

        elif(computer=="scissor" and youstr=="paper"):
                print("you lose!")

        elif(computer=="paper" and youstr=="scissor"):
                print("you win!")

        elif(computer=="rock" and youstr=="scissor"):
                print("you lose!")

        elif(computer=="scissor" and youstr=="rock"):
                    print("you win!")
        else:
                print("Something went wrong try again")
    play_on=input("YOU WANT TO PLAY AGAIN YES/NO:")
    play_on=play_on.lower()