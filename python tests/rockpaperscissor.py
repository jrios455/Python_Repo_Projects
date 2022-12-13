import random
print("Would you like to play a game of rock, paper, scissors?")

player1 = int(input("Pick  1 for rock, 2 for paper, or 3 for scissors?:" ))

computer = random.randint(1,3)

if player1 == 1:
    print('''      
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"''')
elif player1 == 2:
    print('''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        ''')
   
elif player1 == 3:
    print('''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')
if computer == 1:
    print("The computer chose rock"'''       
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"''')
elif computer == 2:
    print('''The computer chose paper
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        ''')
elif computer == 3:
    print("The computer chose scissor"'''
    
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.''')

