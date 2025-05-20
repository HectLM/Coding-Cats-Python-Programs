import random

print("\033[32mPython Tools and Games (PTaG)\033[34m\nV1.1")
print("\033[31mAll answers must be copied \033[3mEXACTLY\033[23m how they are written!\nAlways use letters, unless told otherwise.\nYou can always press F5 to reset.\033[30m\n")
answer=input("Which tool/game would you like?\n\nA:Rock Paper Scissors\nB:Number Guessing\nC:Dice Roller\nD:Calculator\nE:Hangman\n")
if answer=="A":
    RPS = ["Rock", "Paper", "Scissors"]
    RPSP=input("What is your choice? Rock, Paper or Scissors?\n")
    RPSAI=(random.choice(RPS))
    if RPSP=="Rock" and RPSAI=="Paper":
        print("Oh no! Your opponent's choice was paper!")
    elif RPSP=="Rock" and RPSAI=="Scissors":
        print("Well done! Your opponent's choice was scissors!")
    elif RPSP=="Paper" and RPSAI=="Scissors":
        print("Oh no! Your opponent's choice was scissors!")
    elif RPSP=="Paper" and RPSAI=="Rock":
        print("Well done! Your opponent's choice was rock!")
    elif RPSP=="Scissors" and RPSAI=="Rock":
        print("Oh no! Your opponent's choice was rock!")
    elif RPSP=="Scissors" and RPSAI=="Paper":
        print("Well done! Your opponent's choice was paper!")
    else:
        print("It is a tie - you chose the same item!")
    print("\033[31mPress F5 to reset.\033[30m")
if answer=="B":
    Num=random.randint(1,5)
    print(Num)
    guess=int(input("What is my number? (Choose between 1 and 5 (inclusive))\n"))
    if guess==Num:
        print("Well done! You guessed my number!")
    else:
        print ("Oh no! My number was", Num)
    print("\033[31mPress F5 to reset.\033[30m")
if answer=="C":
    print("Your number is", random.randint(1,6))
    print("\033[31mPress F5 to reset.\033[30m")
if answer=="D":
    op=input("What operation would you like?\nA:Addition\nB:Subtraction\nC:Multiplication\nD:Divison\n")
    if op=="A":
        calc1=int(input("What is your first number?\n"))
        calc2=int(input("What is your second number?\n"))
        result=calc1 + calc2
        print("result =", result)
    elif op=="B":
        calc1=int(input("What is your first number?\n"))
        calc2=int(input("What is your second number?\n"))
        result=calc1 - calc2
        print("result =", result)
    elif op=="C":
        calc1=int(input("What is your first number?\n"))
        calc2=int(input("What is your second number?\n"))
        result=calc1 * calc2
        print("result =", result)
    elif op=="D":
        Round=input("Would you like your answer to be rounded to the nearest integer? Y/N\n")
        if Round=="Y":
            calc1=int(input("What is your first number?\n"))
            calc2=int(input("What is your second number?\n"))
            result=calc1 // calc2
        elif Round=="N":
            calc1=int(input("What is your first number?\n"))
            calc2=int(input("What is your second number?\n"))
            result=calc1 / calc2
        print("result =", result)
    print("\033[31mPress F5 to reset.\033[30m")