import random as r

game = ['paper', 'rock', 'scissor']

def userChoice():
    u = input("Enter Your Choice : ")
    if u in game:
        return u
    return 0

def computerChoice():
    c = r.randint(0,2)
    return game[c]

def winnerChoice(user , computer):
    if (user==computer):
        print(f"user   :   {user}        computer   :  {computer}")
        print("Draw")
        print("==================================================")
    
    elif (
        (user=="paper" and computer=="rock") or
        (user=="rock" and computer=="scissor") or
        (user=="scissor" and computer=="paper")
        ):
        print(f"user   :   {user}        computer   :  {computer}")
        print("Win")
        print("==================================================")
        
    elif user==0:
        print("Invaild Input ..!")
    
    else :
        print(f"user   :   {user}        computer   :  {computer}")
        print("Lose")
        print("==================================================")
        
        
print(game)
u = userChoice()
c = computerChoice()
winnerChoice(u,c)