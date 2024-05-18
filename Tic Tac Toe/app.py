import random  # Import random module for bot's random moves
import os      # Import sys module for use methods when cleaning old area
import string  # Import string module for give random chars at game results
import time    # Import time module for wait when erase random chars
# Area of game
area = ['-','-','-',
        '-','-','-',
        '-','-','-']

# Function for cleaning old area
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for Windows ('cls') or Unix/Linux ('clear')

# Function for erase one symbol at game result 
def erase_symbol(text):
    print(text, end='', flush=True)       # write
    time.sleep(0.1)                       # wait 
    print('\b \b', end='', flush=True)    # erase

print("\n")

# List for button configuration
'''
7 8 9
4 5 6
1 2 3
'''
buttons=[7,8,9,4,5,6,1,2,3]

# List for bot choice elements
index=[1,2,3,4,5,6,7,8,9]

# List for keep human's steps
human_step=[]

# List for keep bot's steps
bot_step=[]

# List for game result
game_result=[]

# Counters for end loop in time
count=0     # Counter for whole game
b_count=0   # Counter for bot's moves

# Variable for identity end of game like win,lose or draw
end=0

# Main loop
while count<5 and end==0:    # Count calculate moves and end checks if the game is over

    # Game title
    print("Tic Tac Toe")

    # Loop for show area of game
    for i in range(0,9,3):
        print(area[i],area[i+1],area[i+2])
    
    tester=1 # For break input's loop

    # Loop for input of x 
    while tester:
        x = int(input("Enter the place of x(1-9):"))    # Input for x

        # To check if the bookmarked location is already bookmarked or out of area 
        if x>9 or x<1:
            print("This value is out of area! Try again.")
        elif area[buttons.index(x)] != "x" and area[buttons.index(x)] != "O":
            area[buttons.index(x)]="x"
            tester=0 # Break loop
        else:
            print("This area already bookmarked! Try again.")
    
    clear_screen() # Call erase function
    index.remove(buttons.index(x)+1)    # Remove bookmarked index for bot's next choices
    human_step.append(buttons.index(x)) # Collect human's step
    
    # Conditions for bot's moves
    '''
    First move is random. Second move is depend on human's(user) move. 
    If there are two 'x' in a row, column, or horizontal Bot blok the third one. 
    Also try to make 3 'O' in a row,column or horizontal.
    This is static code , not use ai,it's not perfect but it's work :)
    '''
    if  b_count<4:  # Bot moves smaller than 4 because human (user) begin first
        if count==0:
            bot= random.choice(index) # Bot's first move. It's random index
        
        # Conditions for bot's other moves
        elif b_count>=2:
            if ((0 in bot_step and 1 in bot_step) or (4 in bot_step and 6 in bot_step) or (5 in bot_step and 8 in bot_step)) and 3 in index:
                bot=3
            elif ((0 in bot_step and 2 in bot_step) or (4 in bot_step and 7 in bot_step)) and 2 in index:
                bot=2
            elif ((0 in bot_step and 3 in bot_step) or (2 in bot_step and 4 in bot_step) or (7 in bot_step and 8 in bot_step)) and 7 in index:
                bot=7
            elif ((0 in bot_step and 4 in bot_step) or (2 in bot_step and 5 in bot_step) or (6 in bot_step and 7 in bot_step)) and 9 in index:
                bot=9
            elif ((0 in bot_step and 6 in bot_step) or (4 in bot_step and 5 in bot_step)) and 4 in index:
                bot=4
            elif ((0 in bot_step and 8 in bot_step) or (1 in bot_step and 7 in bot_step) or (2 in bot_step and 6 in bot_step) or (3 in bot_step and 5 in bot_step)) and 5 in index:
                bot=5
            elif ((1 in bot_step and 2 in bot_step) or (3 in bot_step and 6 in bot_step) or (4 in bot_step and 8 in bot_step)) and 1 in index:
                bot=1
            elif ((1 in bot_step and 4 in bot_step) or (6 in bot_step and 8 in bot_step)) and 8 in index:
                bot=8
            elif ((2 in bot_step and 8 in bot_step) or (3 in bot_step and 4 in bot_step)) and 6 in index:
                bot=6
            elif ((0 in human_step and 1 in human_step) or (4 in human_step and 6 in human_step) or (5 in human_step and 8 in human_step)) and 3 in index:
                bot=3
            elif ((0 in human_step and 2 in human_step) or (4 in human_step and 7 in human_step)) and 2 in index:
                bot=2
            elif ((0 in human_step and 3 in human_step) or (2 in human_step and 4 in human_step) or (7 in human_step and 8 in human_step)) and 7 in index:
                bot=7
            elif ((0 in human_step and 4 in human_step) or (2 in human_step and 5 in human_step) or (6 in human_step and 7 in human_step)) and 9  in index:
                bot=9
            elif ((0 in human_step and 6 in human_step) or (4 in human_step and 5 in human_step)) and 4  in index:
                bot=4
            elif ((0 in human_step and 8 in human_step) or (1 in human_step and 7 in human_step) or (2 in human_step and 6 in human_step) or (3 in human_step and 5 in human_step)) and 5  in index:
                bot=5
            elif ((1 in human_step and 2 in human_step) or (3 in human_step and 6 in human_step) or (4 in human_step and 8 in human_step)) and 1  in index:
                bot=1
            elif ((1 in human_step and 4 in human_step) or (6 in human_step and 8 in human_step)) and 8  in index:
                bot=8
            elif ((2 in human_step and 8 in human_step) or (3 in human_step and 4 in human_step)) and 6 in index:
                bot=6
            else:
               bot= random.choice(index) 
        else:
            if ((0 in human_step and 1 in human_step) or (4 in human_step and 6 in human_step) or (5 in human_step and 8 in human_step)) and 3 in index:
                bot=3
            elif ((0 in human_step and 2 in human_step) or (4 in human_step and 7 in human_step)) and 2 in index:
                bot=2
            elif ((0 in human_step and 3 in human_step) or (2 in human_step and 4 in human_step) or (7 in human_step and 8 in human_step)) and 7  in index:
                bot=7
            elif ((0 in human_step and 4 in human_step) or (2 in human_step and 5 in human_step) or (6 in human_step and 7 in human_step)) and 9 in index:
                bot=9
            elif ((0 in human_step and 6 in human_step) or (4 in human_step and 5 in human_step)) and 4  in index:
                bot=4
            elif ((0 in human_step and 8 in human_step) or (1 in human_step and 7 in human_step) or (2 in human_step and 6 in human_step) or (3 in human_step and 5 in human_step)) and 5 in index:
                bot=5
            elif ((1 in human_step and 2 in human_step) or (3 in human_step and 6 in human_step) or (4 in human_step and 8 in human_step)) and  1 in index:
                bot=1
            elif ((1 in human_step and 4 in human_step) or (6 in human_step and 8 in human_step)) and 8  in index:
                bot=8
            elif ((2 in human_step and 8 in human_step) or (3 in human_step and 4 in human_step)) and 6 in index:
                bot=6
            else:
                bot= random.choice(index)

        # To check if the bookmarked location is already bookmarked
        if area[bot-1] != "x" and area[bot-1] != "O":
            area[bot-1]="O"
            index.remove(bot)       # Remove bookmarked element for next moves
            bot_step.append(bot-1)  # Add move on bot step's list for keep bot moves
    # Add 1 counters        
    count+=1     
    b_count+=1

    # Identity the variable 'end'
    if (area[0]=='x' and area[1]== 'x' and area[2]=='x') or (area[3]=='x' and area[4]== 'x' and area[5]=='x') or (area[6]=='x' and area[7]== 'x' and area[8]=='x') or (area[0]=='x' and area[3]== 'x' and area[6]=='x') or (area[1]=='x' and area[4]== 'x' and area[7]=='x') or (area[2]=='x' and area[5]== 'x' and area[8]=='x') or(area[0]=='x' and area[4]== 'x' and area[8]=='x') or (area[2]=='x' and area[4]== 'x' and area[6]=='x'):
        end= 1
    elif (area[0]=='O' and area[1]== 'O' and area[2]=='O') or (area[3]=='O' and area[4]== 'O' and area[5]=='O') or (area[6]=='O' and area[7]== 'O' and area[8]=='O') or (area[0]=='O' and area[3]== 'O' and area[6]=='O') or (area[1]=='O' and area[4]== 'O' and area[7]=='O') or (area[2]=='O' and area[5]== 'O' and area[8]=='O') or(area[0]=='O' and area[4]== 'O' and area[8]=='O') or (area[2]=='O' and area[4]== 'O' and area[6]=='O'):
        end= -1
    
    
# Last print (game result)
for i in range(0,9,3):
        print(area[i],area[i+1],area[i+2])

# Game result
if end==-1:
    game_result=['G','a','m','e',' ','O','v','e','r']
elif end==1:
    game_result=['Y','o','u',' ','w','i','n']
else:
    game_result=['D','r','a','w']

# Presentation of game result
if count>=5 or end != 0:    # Check if game over
    for i in range(len(game_result)):
        for j in range(9):  # Number of symbols before last elements print
            if j <8:        
                text = ''.join(random.choices(string.ascii_lowercase, k=1)) # Random element generator
                erase_symbol(text)   # Call erase symbol function
            else:
                print(game_result[i],end=' ')  # Print symbol in game result