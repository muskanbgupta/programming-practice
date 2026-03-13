import random

#dice rolling game
print("Welcome!\n ----🎲 Dice Rolling Game🎲----")
print("There are two player you and computer")
print("Whichever is greater will win")
print("But anyone one of them get same number at both side will win at the end")
class dice:
   def dice_rolling(self):
      user=input("You Want to play(Y/N):").lower()
      if(user=="yes" or user=="y"):
         self.roll1=random.randint(1,6)
         self.dice1=random.randint(1,6)
         self.roll2=random.randint(1,6)
         self.dice2=random.randint(1,6)
         print(f"Dice Rolled YOUR numbers are:({self.roll1},{self.dice1})")
         print(f"Dice Rolled COMPUTER's numbers are:({self.roll2},{self.dice2})")
         self.add1=self.roll1+self.dice1
         self.add2=self.roll2+self.dice2
         print(f"So your total score is:{self.add1} \nComputer's total score is:{self.add2}")
         
         
      else:
         print("Thank you for playing!")
      
#equality of both computer and user
#if not equal check which is bigger one
class equal(dice):
   def equality(self):
      if self.roll1==self.dice1:
         print(f"YOU win!{self.roll1,self.dice1}")
      elif self.roll2==self.dice2:
         print(f"COMPUTER win!{self.roll2,self.dice2}")

      else:
           if self.add2>self.add1:
               print(f"COMPUTER won!!")
           elif self.add1>self.add2:
            print(f"YOU won!!")
           else:
              print("IT's tie")
   
      
game=equal()
game.dice_rolling()
game.equality()