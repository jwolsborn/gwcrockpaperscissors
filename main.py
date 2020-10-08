import sys

player1 = input("What's your name, Player 1? ")
player2 = input("And your name, Player 2? ")

player1_answer = input("%s, do you want to choose rock, paper or scissors? " % player1)
player2_answer = input("%s, do you want to choose rock, paper or scissors? " % player2)



def compare(answer1, answer2):
    if answer1 == answer2:
        return("") #What message should you return here if both players give the same answer?
    elif answer1 == 'rock':
        if answer2 == 'scissors':
            return("") #What message should you return if answer1 is rock and answer2 is scissors?
        else:
            return("") #Hmmm this one may be tricky...what answer would you return here?
    elif answer1 == 'scissors':
        if answer2 == 'paper':
            return("") #What message would you return if answer1 is scissors and answer2 is paper
        else:
            return("") #What answer would you return here
    
    #We need one more conditional block like the 2 above see if you can figure it out



#Finally we need to call our function inside this print statement with the answers given by the users.  What would we put in the print statement?
print()
