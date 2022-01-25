import random

from numpy import true_divide

def SWG(comp, player):
    if (comp == player):
        return None

    if (comp == "snake" and player == "gun"):
        return True
    elif (comp == "snake" and player == "water"):
        return False
    elif (comp == "water" and player == "snake"):
        return True
    elif (comp == "water" and player == "gun"):
        return False
    elif (comp == "gun" and player == "water"):
        return True
    elif (comp == "gun" and player == "snake"):
        return False

comp_win = 0
player_win = 0

round_n = int(input("How many rounds you want to play : "))

for i in range(round_n):
    choice = ("Sanke","Water","Gun")

    comp = random.randint(0, 2)
    comp = (choice[comp]).lower()

    wrong_choice = True
    player = (input("Enter Your Choice from the Snake, Water, Gun... -->").lower()).strip()
    while wrong_choice:
        if ((player == "snake") or (player == "water") or (player == "gun")):
            # print(player)
            wrong_choice = False
        else:
            print("\nYou select wrong choise! Plz select right choice....")
            player = (input("Enter Your Choice from the Snake, Water, Gun... -->").lower()).strip()

    result = SWG(comp, player)

    if (result == None):
        print(f'''\nThe round  {i+1} 
        The game was tie!.......''')
    elif (result):
        print(f'''\nThe round  {i+1} 
        The computer select {comp} and you select {player}.
        So you win...''')
        player_win += 1
    else: 
        print(f'''\nThe round  {i+1} 
        The computer select {comp} and you select {player}. 
        So you lost...''')
        comp_win += 1

if (comp_win > player_win):
    print(f'''\nThe total result of computer win is {comp_win} and 
    the total result of player win is {player_win}
    So The final winner is computer.... ''')
elif (comp_win < player_win):
    print(f'''\nThe total result of computer win is {comp_win} and 
    the total result of player win is {player_win}
    So The final winner is player.... ''')
else:
    print(f'''\nThe total result of computer win is {comp_win} and 
    the total result of player win is {player_win}
    So The game is tie.... ''')
