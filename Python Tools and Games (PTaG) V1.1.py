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
if answer=="E":
    import os
     
    # Funtion to clear the terminal
    def clear():
        os.system("clear")
     
    # Functuion to print the hangman
    def print_hangman(values):
        print()
        print("\t +--------+")
        print("\t |       | |")
        print("\t {}       | |".format(values[0]))
        print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
        print("\t {}       | |".format(values[4]))
        print("\t{} {}      | |".format(values[5],values[6]))
        print("\t         | |")
        print("  _______________|_|___")
        print("  `````````````````````")
        print()
     
    # Function to print the hangman after winning
    def print_hangman_win():
        print()
        print("\t +--------+")
        print("\t         | |")
     
        print("\t         | |")
        print("\t O       | |")
        print("\t/|\\      | |")
        print("\t |       | |")
        print("  ______/_\\______|_|___")
        print("  `````````````````````")
        print()
     
    # Function to print the word to be guessed
    def print_word(values):
        print()
        print("\t", end="")
        for x in values:
            print(x, end="")
        print() 
     
    # Function to check for win
    def check_win(values):
        for char in values:
            if char == '_':
                return False
        return True    
     
    # Function for each hangman game
    def hangman_game(word):
     
        clear()
     
        # Stores the letters to be displayed
        word_display = []
     
        # Stores the correct letters in the word
        correct_letters = []
     
        # Stores the incorrect guesses made by the player
        incorrect = []
     
        # Number of chances (incorrect guesses)
        chances = 0
     
        # Stores the hangman's body values
        hangman_values = ['O','/','|','\\','|','/','\\']
     
        # Stores the hangman's body values to be shown to the player
        show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
     
        # Loop for creating the display word
        for char in word:
            if char.isalpha():
                word_display.append('_')
                correct_letters.append(char.upper())
            else:
                word_display.append(char)
     
        # Game Loop         
        while True:
     
            # Printing necessary values
            print_hangman(show_hangman_values)
            print_word(word_display)            
            print()
            print("Incorrect characters : ", incorrect)
            print()
     
     
            # Accepting player input
            inp = input("Enter a character = ")
            if len(inp) != 1:
                clear()
                print("Wrong choice!! Try Again")
                continue
     
            # Checking whether it is a alphabet
            if not inp[0].isalpha():
                clear()
                print("Wrong choice!! Try Again")
                continue
     
            # Checking if it already tried before   
            if inp.upper() in incorrect:
                clear()
                print("Already tried!!")
                continue   
     
            # Incorrect character input 
            if inp.upper() not in correct_letters:
                 
                # Adding in the incorrect list
                incorrect.append(inp.upper())
                 
                # Updating the hangman display
                show_hangman_values[chances] = hangman_values[chances]
                chances = chances + 1
                 
                # Checking if the player lost
                if chances == len(hangman_values):
                    print()
                    clear()
                    print("\tGAME OVER!!!")
                    print_hangman(hangman_values)
                    print("The word is :", word.upper())
                    break
     
            # Correct character input
            else:
     
                # Updating the word display
                for i in range(len(word)):
                    if word[i].upper() == inp.upper():
                        word_display[i] = inp.upper()
     
                # Checking if the player won        
                if check_win(word_display):
                    clear()
                    print("\tCongratulations! ")
                    print_hangman_win()
                    print("The word is :", word.upper())
                    break
            clear() 
         
     
    if __name__ == "__main__":
     
        clear()
     
        # Types of categories
        topics = {1: "DC characters", 2:"Marvel characters", 3:"Anime characters"}
     
        # Words in each category
        dataset = {"DC characters":["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN", "MARTIAN MANHUNTER", "BATMAN"],\
                     "Marvel characters":["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
                     "Anime characters":["MONKEY D. LUFFY", "RORONOA ZORO", "LIGHT YAGAMI", "MIDORIYA IZUKU"]
                     }
         
        # The GAME LOOP
        while True:
     
            # Printing the game menu
            print()
            print("-----------------------------------------")
            print("\t\tGAME MENU")
            print("-----------------------------------------")
            for key in topics:
                print("Press", key, "to select", topics[key])
            print("Press", len(topics)+1, "to quit")    
            print()
             
            # Handling the player category choice
            try:
                choice = int(input("Enter your choice = "))
            except ValueError:
                clear()
                print("Wrong choice!!! Try again")
                continue
     
            # Sanity checks for input
            if choice > len(topics)+1:
                clear()
                print("No such topic!!! Try again.")
                continue   
     
            # The EXIT choice   
            elif choice == len(topics)+1:
                print()
                print("Thank you for playing!")
                break
     
            # The topic chosen
            chosen_topic = topics[choice]
     
            # The word randomly selected
            ran = random.choice(dataset[chosen_topic])
     
            # The overall game function
            hangman_game(ran)
