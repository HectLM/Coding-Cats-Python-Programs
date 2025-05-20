import random

print("\033[32mPython Tools and Games (PTaG)\033[34m\nV2.0.1")
print("\033[31mAll answers must be copied \033[3mEXACTLY\033[23m how they are written! (Capitals do not matter).\nAlways use letters, unless told otherwise.\nYou can always press F5 to reset.\033[30m\n")
start=input("Are you ready to start? Input 'Y' or 'N'\n")
if start=="N":
    exit("Bro did not even try it")
elif start=="Y":
    print("Welcome")
else:
    print("I will take that as a 'Yes'")
answer=input("Which tool/game would you like?\n\nA:Rock Paper Scissors\nB:Number Guessing\nC:Dice Roller\nD:Calculator\nE:Hangman\nF:Snake\nG:Warrior Cats stuff =^_^=\n")
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
        print("Result =", result)
    elif op=="B":
        calc1=int(input("What is your first number?\n"))
        calc2=int(input("What is your second number?\n"))
        result=calc1 - calc2
        print("Result =", result)
    elif op=="C":
        calc1=int(input("What is your first number?\n"))
        calc2=int(input("What is your second number?\n"))
        result=calc1 * calc2
        print("Result =", result)
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
        print("Result =", result)
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
if answer=="F".lower():
    
    import turtle
     
    w = 500
    h = 500
    food_size = 10
    delay = 100
     
    offsets = {
        "up": (0, 20),
        "down": (0, -20),
        "left": (-20, 0),
        "right": (20, 0)
    }
     
    def reset():
        global snake, snake_dir, food_position, pen
        snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        snake_dir = "up"
        food_position = get_random_food_position()
        food.goto(food_position)
        move_snake()
         
    def move_snake():
        global snake_dir
     
        new_head = snake[-1].copy()
        new_head[0] = snake[-1][0] + offsets[snake_dir][0]
        new_head[1] = snake[-1][1] + offsets[snake_dir][1]
     
         
        if new_head in snake[:-1]:
            reset()
        else:
            snake.append(new_head)
     
         
            if not food_collision():
                snake.pop(0)
     
     
            if snake[-1][0] > w / 2:
                snake[-1][0] -= w
            elif snake[-1][0] < - w / 2:
                snake[-1][0] += w
            elif snake[-1][1] > h / 2:
                snake[-1][1] -= h
            elif snake[-1][1] < -h / 2:
                snake[-1][1] += h
     
     
            pen.clearstamps()
     
             
            for segment in snake:
                pen.goto(segment[0], segment[1])
                pen.stamp()
     
             
            screen.update()
     
            turtle.ontimer(move_snake, delay)
     
    def food_collision():
        global food_position
        if get_distance(snake[-1], food_position) < 20:
            food_position = get_random_food_position()
            food.goto(food_position)
            return True
        return False
     
    def get_random_food_position():
        x = random.randint(- w / 2 + food_size, w / 2 - food_size)
        y = random.randint(- h / 2 + food_size, h / 2 - food_size)
        return (x, y)
     
    def get_distance(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance
    def go_up():
        global snake_dir
        if snake_dir != "down":
            snake_dir = "up"
     
    def go_right():
        global snake_dir
        if snake_dir != "left":
            snake_dir = "right"
     
    def go_down():
        global snake_dir
        if snake_dir!= "up":
            snake_dir = "down"
     
    def go_left():
        global snake_dir
        if snake_dir != "right":
            snake_dir = "left"
     
     
    screen = turtle.Screen()
    screen.setup(w, h)
    screen.title("Snake")
    screen.bgcolor("blue")
    screen.setup(500, 500)
    screen.tracer(0)
     
     
    pen = turtle.Turtle("square")
    pen.penup()
     
     
    food = turtle.Turtle()
    food.shape("square")
    food.color("yellow")
    food.shapesize(food_size / 20)
    food.penup()
     
     
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
     
     
    reset()
    turtle.done()

if answer=="G":
    WCS=input("Would you like:\nA:Warrior Cats Name Generator\nB:Warrior Cats Quiz\n")
    if WCS=="A":
        #print("|\---/|\n| o_o |\n \_^_/")
        role=input("What role are you?\nKit\nApprentice\nWarrior\nLeader\n")
        if role=="Kit":
            suffix="kit"
        elif role=="Apprentice":
            suffix="paw"
        elif role=="Warrior":
            warriorSuffix = ["tail", "leaf", "heart", "claw", "storm", "stripe", "wind", "pelt", "fur", "face", "flower", "ear", "eye"]
            suffix=(random.choice(warriorSuffix))
        elif role=="Leader":
            suffix="star"
        else:
            print("\033[31mInvalid\033[30m - press \033[31mF5\033[30m and reset")
        if suffix!="N":
            prefix_choices = ["Blue", "Red", "Dust", "Spotted", "Lion", "Grey", "Tiger", "Raven", "White", "Sand", "Dark", "Long", "Running", "Willow", "Mouse", "Fire", "Frost", "Brindle", "Golden", "Speckle", "Half", "Small", "Patch", "One", "Dapple"]
            prefix=(random.choice(prefix_choices))
            print("Your Warrior Cat name is:\n"+prefix+suffix)
            print("Press \033[31mF5\033[30m to reset")
    elif WCS=="B":
        q1a=input("Ready? Go!\nQ1: Who is the protagonist from series 1-4?\nA:Tigerstar\nB:Firestar\nC:Bluestar\n")
        if q1a=="A" or q1a=="C":
            print("Incorrect. The correct answer was B - Firestar.")
        elif q1a=="B":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was B - Firestar.")
        q2a=input("Q2: How many series are there?\nA:9\nB:7\nC:4\n")
        if q2a=="B" or q2a=="C":
            print("Incorrect. The correct answer was A - 9.")
        elif q2a=="A":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was A - 9.")
        q3a=input("Q3: How many ORIGINAL clans are there (excluding Starclan)?\nA:4\nB:7\nC:5\n")
        if q3a=="A" or q3a=="B":
            print("Incorrect. The correct answer was C - 5.")
        elif q3a=="C":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was C - 5.")
        q4a=input("Q4: Which cat has NEVER caught a piece of prey before?\nA:Squirrelflight\nB:Leafpool\nC:Alderheart\n")
        if q4a=="A" or q4a=="B":
            print("Incorrect. The correct answer was C - Alderheart.")
        elif q4a=="C":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was C - Alderheart.")