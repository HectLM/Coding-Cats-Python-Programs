import random, time

global slots,level,money,load

slots = ['loss', 'loss', '5', '5', '5', '5', '10', '10', '20', '20', '30', '30', '100']
level = 1
money = 0
load = 5

def intro(slots,level,money,load):
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
    time.sleep(4)

    print('\nWelcome to Jackpot Simulator!')
    time.sleep(5)
    main(slots,level,money,load)

def main(slots,level,money,load):
    b = input(f'''
Total money: £{money}
Press "ENTER" to play, or "S" to go to the shop
>>> ''')
    if b.lower() == 's':
        d = input('''
A: Level Up
B: Decrease waiting time
>>> ''')
        if d.lower() == 'a':
            luc = 10**level
            c = input(f'Level up cost: £{luc}. Would you like to level up? [Y/N]\n>>> ')
            if c.lower() == 'y':
                if luc > money:
                    print('You can\'t afford that!')
                    time.sleep(1)
                    main(slots,level,money,load)
                else:
                    money = money - luc
                    level = level + 1
                    main(slots,level,money,load)
            else:
                main(slots,level,money,load)
        elif d.lower() == 'b':
            if load == 0:
                print('Max upgrade reached!')
                time.sleep(1)
                main(slots,level,money,load)
            duc = load = 100 - (load*5)
            e = input(f'Decrease waiting time cost: £{duc}. Would you like to decrease waiting time? [Y/N]\n>>> ')
            if e.lower() == 'y':
                if duc > money:
                    print('You can\'t afford that!')
                    time.sleep(1)
                    main(slots,level,money,load)
                else:
                    money = money - duc
                    load = load - 0.5
                    main(slots,level,money,load)
            else:
                main(slots,level,money,load)
    else:
        a = random.choice(slots)
        print('Please wait...')
        time.sleep(load)
        if a == 'loss':
            'You lost! Better luck next time...'
        elif a == '5':
            earned = 5*level
            money = money + earned
            print(f'You won £{earned}!')
        elif a == '10':
            earned = 10*level
            money = money + earned
            print(f'You won £{earned}!')
        elif a == '20':
            earned = 20*level
            money = money + earned
            print(f'You won £{earned}!')
        elif a == '30':
            earned = 30*level
            money = money + earned
            print(f'You won £{earned}!')
        elif a == '100':
            earned = 100*level
            money = money + earned
            print(f'JACKPOT! You won £{earned}!')
        time.sleep(1)
        main(slots,level,money,load)

#intro(slots,level,money,load)
main(slots,level,money,load)