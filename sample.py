import random as rd

#computer-Choice = x
#user-Choice = y

choices={
     1:"rock",
     2:"paper",
     3:"scissors"
}

rounds=0
Xp=0
Yp=0

print("ROCK_PAPER_SCISSORS\n\n""Winning Rules as follows:\nRock vs paper - paper wins\nRock vs scissor - Rock wins\npaper vs scissor - scissor wins")
print("TYPE:\n1-rock\n2-paper\n3-scissors\n\n")

rounds=int(input("Enter the rounds that you wanna play: "))

for i in range(0,rounds):
     print("\n\nRound:",i+1,"\n")
     x=rd.randint(1,3)
     y=int(input("Enter your choice: "))
     print("Your choice =",choices.get(y))
     print("Computer choice =",choices.get(x))
     if y==x+1:
          Yp=Yp+1
          print("You won")
     elif x==y+1:
          Xp=Xp+1
          print("You lost")
     elif x==y:
          print("equal! doesn't count")
     else:
          prior= True if y==x+2 else False
          match prior:
               case True:
                     Xp=Xp+1
                     print("You lost")
               case False: 
                     Yp=Yp+1
                     print("You won")
     print("\nSCORE BOARD: \nYou:",Yp,"\nBot:",Xp)

if Yp>Xp:
     print("CONGRATZ! YOU WON THE GAME\n")
elif Xp>Yp:
     print("HAHA! YOU LOST\n")
else:
     print("Somehow, you guys scored equal!\n")
