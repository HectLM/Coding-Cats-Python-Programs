#Hector Mangwana
#06/09/24
#EFM P1

#Imports
import time, random

def showInstructions():
    #print a main menu and the commands
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
https://www.codingcats.co.uk''')
    time.sleep(4)
    
    print('''
Escape From Mars - Part 1: The Base
 _______ _    _ ______   ____           _____ ______         
|__   __| |  | |  ____| |  _ \   /\    / ____|  ____|    _   
   | |  | |__| | |__    | |_) | /  \  | (___ | |__     _| |_ 
   | |  |  __  |  __|   |  _ < / /\ \  \___ \|  __|   |_   _|
   | |  | |  | | |____  | |_) / ____ \ ____) | |____    |_|  
 _ |_|_ |_|__|_|______| |____/_/__ _\_\_____/|______|        
| |  | |  __ \|  __ \   /\|__   __|  ____|                   
| |  | | |__) | |  | | /  \  | |  | |__                      
| |  | |  ___/| |  | |/ /\ \ | |  |  __|                     
| |__| | |    | |__| / ____ \| |  | |____                    
 \____/|_|    |_____/_/    \_\_|  |______|
 
 CURRENT VERSION: 2.1.1
 ''')
    time.sleep(5)
    input('''
========

Unlock the outside and get the Oxidation Potion to escape
the Base!
Avoid the hungry monster in the kitchen!
There are 3 possible endings!
(NOTE: This game is designed for you to memorise the layout of the map, like a maze!)
(There is also a secret hidden in the map!)
SEQUEL: ESCAPE FROM MARS P2

========
Commands:
    go [north, south, east, west]
    get [item]

Press 'ENTER/RETURN' to begin!
''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                'south' : 'Kitchen',
                'east' : 'Dining Room',
                'item' : 'key'
            },

            'Kitchen' : {
                'north' : 'Hall',
                'item' : 'monster'
            },
            
            'Dining Room' : {
                'north' : 'Secret Room',
                'west' : 'Hall',
                'south' : 'Outside',
                'item' : 'potion'
            },
            
            'Outside' : {
                'north' : 'Dining Room'
            },
            
            'Secret Room' : {
                'south' : 'Dining Room',
                'item' : 'bundle'
            }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()
age = input('''How old are you?
[THIS INFORMATION IS REQUIRED TO KEEP THE GAME AGE APPROPRIATE FOR YOU]
>>> ''')

#loop forever
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #E.G. typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>>> ')
    
    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
        

    #if they type 'get' first
    elif move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #SECRET
            if move[1] == 'potion':
                print("You suddenly feel more powerful...")
            if move[1] == 'bundle':
                inventory.remove('bundle')
                inventory.append('potion')
                inventory.append('cookie')
                inventory.remove('SecretKey')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    else:
        print('Not valid input')
    
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'potion' not in inventory:
        if int(age) < 12:
            deaths = ['YOU WERE CAUGHT BY A MONSTER...', 'YOU WERE SEEN BY A MONSTER...']
        else:
            deaths = ['A monster picked you up and snapped your neck...', 'A monster picked you up and ate you whole...', 'A monster picked you up and repeatedly smashed you on the ground...', 'A monster picked you up and threw you at the wall...', 'A monster picked you up and threw you outside with no oxygen...']
        death = random.choice(deaths)
        print(death + " YOU GOT THE BAD ENDING!")
        exit('Thank you for playing!')
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'potion' in inventory:
        print('The potion helped you defeat the monster!')
        del rooms[currentRoom]['item']
        inventory.remove('potion')
        inventory.append('SecretKey')
    
    #if the player does not have the key or potion
    if currentRoom == 'Outside' and 'key' not in inventory and 'potion' not in inventory:
        print("You can't go that way yet!")
        currentRoom = 'Dining Room'
    #if the player escaps with the cookie
    elif currentRoom == 'Outside' and 'key' in inventory and 'potion' in inventory and 'cookie' in inventory:
        print('You escaped the house... YOU GOT THE COOKIE ENDING!')
        exit("Thanks for Playing")
    #if the player escapes without the cookie
    elif currentRoom == 'Outside' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU GOT THE NORMAL ENDING!')
        exit("Thanks for Playing")
    
    #Secret Room code
    if currentRoom == 'Secret Room' and 'SecretKey' in inventory:
        print("You found the secret room!")
    elif currentRoom == 'Secret Room' and 'SecretKey' not in inventory:
        print("You can't go that way yet!")
        currentRoom = 'Dining Room'     