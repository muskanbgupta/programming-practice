import random
y="yes"
while y=="yes" or "y":
    ludo=random.choice((1,2,3,4,5,6))
    
    match (ludo):
        case 1:
            print(" _____")
            print("|     |\n|  0  |\n|_____|")
        case 2:
            print(" _____")
            print("|0    |\n|     |\n|____0|")
        case 3:
            print(" _____")
            print("|0    |\n|  0  |\n|____0|")
        case 4:
            print(" _____")
            print("|0   0|\n|     |\n|0___0|")
        case 5:
            print(" _____")
            print("|0   0|\n|  0  |\n|0___0|")
        case 6:
            print(" _____")
            print("|0 0 0|\n|0 0 0|\n|0_0_0|")
    y=input("play again?\nENTER").lower()