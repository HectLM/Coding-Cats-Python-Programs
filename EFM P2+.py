#Hector Mangwana
#11/10/24
#EFM P2

#imports
import random, time

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
Escape From Mars - Part 2: The Spaceship
========
 _______ _    _ ______                                               
|__   __| |  | |  ____|                                              
   | |  | |__| | |__                                                 
   | |  |  __  |  __|                                                
   | |  | |  | | |____                                               
  _|_|_ |_|__|_|______|___ ______  _____ _    _ _____ _____          
 / ____|  __ \ /\   / ____|  ____|/ ____| |  | |_   _|  __ \     _   
| (___ | |__) /  \ | |    | |__  | (___ | |__| | | | | |__) |  _| |_ 
 \___ \|  ___/ /\ \| |    |  __|  \___ \|  __  | | | |  ___/  |_   _|
 ____) | |  / ____ \ |____| |____ ____) | |  | |_| |_| |        |_|  
|_____/|_|_/_/ ___\_\_____|______|_____/|_|  |_|_____|_|             
| |  | |  __ \|  __ \   /\|__   __|  ____|                           
| |  | | |__) | |  | | /  \  | |  | |__                              
| |  | |  ___/| |  | |/ /\ \ | |  |  __|                             
| |__| | |    | |__| / ____ \| |  | |____                            
 \____/|_|    |_____/_/    \_\_|  |______|
 ''')
    time.sleep(5)
    
    input('''
CURRENT VERSION: 2.0.1
========

Fix the Spaceship to escape Mars!
(NOTE: This game is designed for you to memorise the layout of the map, like a maze!)
SEQUEL: 'EFM P3: A New Planet'

========
Commands:
    go [north, south, east, west, up, down]
       (You will be told if you can go up/down - be sure to look out for it!)
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
    print('---------------------------\nENGINE STATUS:', engine_status)
    print('---------------------------')

#an inventory, which is initially empty
inventory = []

#engine status
engine_status = 'BROKEN'

#a dictionary linking a room to other rooms
rooms = {

            'Airlock' : { 
                'north' : 'Hall',
                'south' : 'Outside'
                },

            'Hall' : {
                'west' : 'Control Room',
                'north' : 'Sleeping Quarters',
                'east' : 'Kitchen'
                },
            
            'Control Room' : {
                'east' : 'Hall',
                'down' : 'Engine Room'
                },
            
            'Sleeping Quarters' : {
                'south' : 'Hall'
                },
            
            'Engine Room' : {
                'up' : 'Control Room',
                'item' : 'key'
                },
            
            'Kitchen' : {
                'west' : 'Hall',
                'item' : 'marshmallow'
                },
            
            'Outside' : {
                'item' : 'monster'
                }

         }

#start the player in the Airlock
currentRoom = 'Airlock'

showInstructions()

#loop forever
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
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
    elif move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    else:
        print('Invalid input')
        
    #Code for Bad Ending        
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print("You went outside and suffocated... YOU (somehow) GOT THE BAD ENDING!")
        exit('YOU LOSE! Thank you for playing!')   
            
    #stuff depending on the room you are in
    if currentRoom == 'Control Room':
        if engine_status != 'FIXED':
            print("You are able to go down!")
        elif engine_status == 'FIXED':
            print('You escaped Mars - YOU GOT THE NORMAL ENDING!')
            time.sleep(1)
            print('''You are flying your ship back to Earth.
Suddenly, you see Jupiter and realise the map is upside down!
You are almost out of Coding Cats Rocket Fuel™, so you decide to land.
Now, you need a way to produce more Coding Cats Rocket Fuel™!''')
            exit('YOU WIN! Thank you for playing!')
        
    elif currentRoom == 'Engine Room':
        print("You are able to go up!")
        if 'spanner' in inventory:
            print("You used the spanner!")
            inventory.remove('spanner')
            engine_status = 'FIXED'
            print('''---------------------------
Go up to win!''')
        else:
            print('You don\'t have the item that you need')
        
    elif currentRoom == 'Sleeping Quarters':
        input('''You see a few martians.
They have the spanner you need to repair the engine.
They also want a marshmallow
Press 'ENTER/RETURN' to continue
----------------------------
----------------------------''')
        if 'marshmallow' in inventory:
            print("You gave them the marshmallow!")
            inventory.remove('marshmallow')
            inventory.append('spanner')
            currentRoom = 'Hall'
            del rooms[currentRoom]['north']
        else:
            print('You don\'t have the item that you need')
            
    elif currentRoom == 'Kitchen':
        if 'key' not in inventory and 'marshmallow' in inventory:
            print('Go to the Sleeping Quarters.')
        elif 'key' in inventory:
            print('You used the key!')
            inventory.remove('key')
        elif 'key' not in inventory:
            print('You need a key!')
            currentRoom = 'Hall'
    
    elif currentRoom == 'Hall':
        if 'marshmallow' in inventory:
            del rooms[currentRoom]['east']
            