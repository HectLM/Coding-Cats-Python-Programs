import random, time, turtle, math, os

print('''This is a

 ██████╗ ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔════╝██╔═══██╗██╔══██╗██║████╗  ██║██╔════╝ 
██║     ██║   ██║██║  ██║██║██╔██╗ ██║██║  ███╗
██║     ██║   ██║██║  ██║██║██║╚██╗██║██║   ██║
╚██████╗╚██████╔╝██████╔╝██║██║ ╚████║╚██████╔╝
 ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                               
 ██████╗ █████╗ ████████╗███████╗              
██╔════╝██╔══██╗╚══██╔══╝██╔════╝              
██║     ███████║   ██║   ███████╗              
██║     ██╔══██║   ██║   ╚════██║              
╚██████╗██║  ██║   ██║   ███████║              
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝              

Python Program - Enjoy!
https://www.codingcats.co.uk (Copy and paste into browser, as it is marked as 'UNSECURED')''')
time.sleep(2)

print("\033[32mPython Tools and Games (PTaG)\033[34m\nV3.1")
print("\033[31mAll answers must be copied \033[3mEXACTLY\033[23m how they are written! (Capitals do not matter).\nAlways use singular letters, unless told otherwise.\nYou can always press F5 to reset.\033[0m\n")
start=input("Are you ready to start? Input 'Y' or 'N'\n")
if start.lower()=="n":
    print("Too bad.")
elif start.lower()=="y":
    print("Welcome!")
else:
    print("I will take that as a 'Yes'")
answer=input("\nWhich tool/game would you like?\n\nA: Rock Paper Scissors\nB: Number Guessing\nC: Dice Roller\nD: Calculator\nE: Hangman\nF: Snake\nG: Warrior Cats stuff (\033[32mNAME GENERATOR UPDATE\033[0m)(\033[32mNEW WCUE NAME FORMATTER\033[0m)\nH: Noughts And Crosses AI\n")
if answer.lower()=="a":
    RPS = ["Rock", "Paper", "Scissors"]
    RPSP=input("What is your choice? Rock, Paper or Scissors?\n")
    RPSAI=(random.choice(RPS))
    if RPSP.lower()=="rock" and RPSAI=="Paper":
        print("Oh no! Your opponent's choice was paper!")
    elif RPSP.lower()=="rock" and RPSAI=="Scissors":
        print("Well done! Your opponent's choice was scissors!")
    elif RPSP.lower()=="paper" and RPSAI=="Scissors":
        print("Oh no! Your opponent's choice was scissors!")
    elif RPSP.lower()=="paper" and RPSAI=="Rock":
        print("Well done! Your opponent's choice was rock!")
    elif RPSP.lower()=="scissors" and RPSAI=="Rock":
        print("Oh no! Your opponent's choice was rock!")
    elif RPSP.lower()=="scissors" and RPSAI=="Paper":
        print("Well done! Your opponent's choice was paper!")
    else:
        print("It is a tie - you chose the same item!")
    exit("Press F5 to reset.")
if answer.lower()=="b":
    a=input("Choose a difficulty:\nA: Easy\nB: Medium\nC: Hard\n>>> ")
    if a.lower()=="a":
        num=5
    elif a.lower=="b":
        num=7
    elif a.lower()=="c":
        num=10
    Num=random.randint(1,num)
    guess=int(input(f"What is my number? (Choose between 1 and {num} (inclusive))\n")) #One line that is compatible with any difficulty
    if guess==Num:
        print("Well done! You guessed my number!")
    else:
        print ("Oh no! My number was", Num)
    exit("Press F5 to reset.")
if answer.lower()=="c":
    a=input("What die do you want?\nA: D4\nB: D6\nC: D8\nD: D10\nE: D12\nF: D20\n>>> ") #Multiple options for D&D
    if a.lower()=="a":
        num=4
    elif a.lower()=="b":
        num=6
    elif a.lower()=="c":
        num=8
    elif a.lower()=="d":
        num=10
    elif a.lower()=="e":
        num=12
    elif a.lower()=="f":
        num=20
    else:
        exit("Invalid. Press F5 to reset.")
    print("You rolled a", random.randint(1,num))
    exit("Press F5 to reset.")
if answer.lower()=="d":
    operations = {
        "a": ("Addition", lambda x, y: x + y),
        "b": ("Subtraction", lambda x, y: x - y),
        "c": ("Multiplication", lambda x, y: x * y),
        "d": ("Division", lambda x, y: x / y),
        "r": ("Rounded Division", lambda x, y: x // y),
        "e": ("Exponentiation", lambda x, y: x ** y),
        "s": ("Square Root", lambda x: math.sqrt(x)),
        "m": ("Modulo", lambda x, y: x % y),
        "p": ("Percentage", lambda x, y: (x / y) * 100)
    }

    op = input("Choose an operation:\nA: Addition\nB: Subtraction\nC: Multiplication\nD: Division\nR: Rounded Division\nE: Exponentiation\nS: Square Root\nM: Modulo\nP: Percentage\n").lower()

    if op in operations:
        if op == "s":  # Square root only needs one number
            calc1 = float(input("Enter a number: "))
            result = operations[op][1](calc1)
        else:
            calc1 = float(input("Enter first number: "))
            calc2 = float(input("Enter second number: "))
            result = operations[op][1](calc1, calc2)

        print(f"Result: {result}")

    else:
        print("Invalid selection. Please try again.")

    exit("Press F5 to reset.")
    
    
if answer.lower()=="e":

    # Function to clear the terminal
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
        topics = {1: "Noob Variants", 2: "Mineral"}
     
        # Words in each category
        dataset = {"Noob Variants":["BASIC", "TALL", "BIG", "SMALL", "NANO", "OOOOOOOOMEGA", "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMEGAAAAAAAAAAAAHHHHHHHHHHHH", "FLYING", "BOMBARDER"],\
                     "Mineral":["BASIC", "SILVER", "GOLD", "DIAMOND", "EMERALD", "RUBY", "AMETHYST"]
                     }
         
        # The GAME LOOP
        while True:
     
            # Printing the game menu
            print()
            print("-----------------------------------------")
            print("\t\tGAME MENU - Roblox SAEN Hangman!")
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
if answer.lower()=="f":

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


if answer.lower()=="g":
    WCS=input("Would you like:\nA: Warrior Cats Name Generator (V1.1)\nB: Warrior Cats Quiz (V1.0)\nC: WCUE Name Formatter\n")
    if WCS.lower()=="a":
        role=input("What role are you?\nKit\nApprentice\nWarrior\nLeader\n")
        if role.lower()=="kit":
            suffix="kit"
        elif role.lower()=="apprentice":
            suffix="paw"
        elif role.lower()=="warrior":
            warriorSuffix = ["tail", "leaf", "heart", "claw", "storm", "stripe", "wind", "pelt", "fur", "face", "flower", "ear", "eye", "foot", "nose", "face", "cloud", "heart", "fang"]
            suffix=(random.choice(warriorSuffix))
        elif role.lower()=="leader":
            suffix="star"
        else:
            exit("Invalid - press F5 to reset")
        if suffix!="N":
            prefix_choices = ["Blue", "Red", "Dust", "Spotted", "Lion", "Grey", "Tiger", "Raven", "White", "Sand", "Dark", "Long", "Running", "Willow", "Mouse", "Fire", "Frost", "Brindle", "Golden", "Speckle", "Half", "Small", "Patch", "One", "Dapple", "Black", "Stumpy", "Brown", "Wet", "Claw", "Little", "Night", "Dawn", "Ash", "Tall", "Crooked", "Oak", "Yellow"]
            prefix=(random.choice(prefix_choices))
            print(f"\nYour Warrior Cat name is:\n{prefix}'{suffix}")
            exit("Press F5 to reset")
    elif WCS.lower()=="b":
        q1a=input("Ready? Go!\nQ1: Who is the protagonist from series 1-4?\nA:Tigerstar\nB:Firestar\nC:Bluestar\n")
        if q1a.lower()=="a" or q1a.lower()=="c":
            print("Incorrect. The correct answer was B - Firestar.")
        elif q1a.lower()=="b":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was B - Firestar.")
        q2a=input("Q2: How many series are there?\nA:9\nB:7\nC:4\n")
        if q2a.lower()=="b" or q2a.lower()=="c":
            print("Incorrect. The correct answer was A - 9.")
        elif q2a.lower()=="a":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was A - 9.")
        q3a=input("Q3: How many ORIGINAL clans are there (excluding Starclan)?\nA:4\nB:7\nC:5\n")
        if q3a.lower()=="a" or q3a.lower()=="b":
            print("Incorrect. The correct answer was C - 5.")
        elif q3a.lower()=="c":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was C - 5.")
        q4a=input("Q4: Which cat has NEVER caught a piece of prey before?\nA:Squirrelflight\nB:Brambleclaw\nC:Alderheart\n")
        if q4a.lower()=="a" or q4a.lower()=="b":
            print("Incorrect. The correct answer was C - Alderheart.")
        elif q4a.lower()=="c":
            print("Correct!")
        else:
            print("That was not an option. The correct answer was C - Alderheart.")
        exit("Press F5 to reset.")
    elif WCS.lower()=="c":
        name=input("Input your Warrior Cat name: ")
        print(f"Formatted name: //[{name}]\\\\") # '\\' appears as '\', so '\\\\' appears as '\\'
        exit("Press F5 to reset.")

if answer.lower()=="h": #Code is cleaner because I came back to this project after a while learning more Python
    # Define color codes
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    # Board representation (numbered 1-9)
    board = [" " for _ in range(9)]

    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # Print the board with centered numbers (while preserving the shape)
    def print_board():
        print("\n")
        for i in range(0, 9, 3):
            print(f" {colorize(board[i], i+1)} | {colorize(board[i+1], i+2)} | {colorize(board[i+2], i+3)} ")
            if i < 6:
                print("---+---+---")  # Keeps board properly aligned
        print("\n")

    # Function to colorize Xs and Os while displaying centered numbers for empty spaces
    def colorize(symbol, pos):
        if symbol == "X":
            return f"{RED}X{RESET}"  # Keep X centered
        elif symbol == "O":
            return f"{BLUE}O{RESET}"  # Keep O centered
        else:
            return str(pos)  # Show position number instead of empty space

    # Check for winner
    def check_winner(player):
        for combo in win_combinations:
            if all(board[i] == player for i in combo):
                return True
        return False

    # Minimax AI algorithm
    def minimax(is_maximizing):
        if check_winner("O"): return -1
        if check_winner("X"): return 1
        if " " not in board: return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = minimax(False)
                    board[i] = " "
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(True)
                    board[i] = " "
                    best_score = min(best_score, score)
            return best_score

    # AI move using minimax
    def ai_move():
        best_score = -float("inf")
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        board[best_move] = "X"

    # Game loop
    def n_c():
        print("Welcome to Noughts And Crosses!")
        print_board()
        
        for turn in range(9):
            if turn % 2 == 0:
                move = int(input("Enter your move (1-9): ")) - 1  # Adjust input to match indexing
                if board[move] == " ":
                    board[move] = "O"
                else:
                    print("Invalid move. Try again.")
                    continue
            else:
                ai_move()

            print_board()
            
            if check_winner("O"):
                print("You win!")
                return
            elif check_winner("X"):
                print("AI wins!")
                return

        print("It's a draw!")

    # Start the game
    n_c()
