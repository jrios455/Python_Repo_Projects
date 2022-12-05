print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to The Adventure Game!")
print("Your mission is to find the treasure")

first_level = input("You have arrived to a turn, do you want to go left or right?: ").lower()
if first_level == "left":
    second_level = input("You have made it to the next level! You have arrived at a body of water..Do you want to swim or wait?: ").lower()
    if second_level == "wait":
        third_level = input("You have made it to an island with three doors. Red, Blue, and Green.. Which door do you choose?: ").lower()
        if third_level == "green":
            print("You have found the treasure!")
        elif third_level == "blue":
            print("You released the island monster and it devoured you! GAME OVER!!")
        elif third_level == "red":
            print("You entered a room full of poisnous snakes!! GAME OVER!!")
    else:
        print("GAME OVER!!")
else:
    print("You fell into a trap! GAME OVER!")













        


