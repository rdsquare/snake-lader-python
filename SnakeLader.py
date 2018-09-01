'''
    Snake Lader game in python with terminal interface
    Copyright (C) 2018 Rahul Dangi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''



''' This is Snake Lader game
It will accept no. of player and then assign all to zero
It will use random number generation for dice throwing
'''
print('''
    Snake Lader  Copyright (C) 2018  Rahul Dangi
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions;
''')

import random #it will be used to generate random no. for dice (1-6)
snakeM = [17, 54, 62, 64, 87, 93, 95, 99] #This point where snake's mouth is available
snakeT = [7, 34, 19, 60, 24, 73, 75, 78] #This point where snake's tail is available
laderB = [4, 9, 20, 28, 40, 51, 63, 71] #This is Base of the lader
laderT = [14, 31, 38, 84, 59, 67, 81, 91] #This is top of the lader
playerList = [] #It will store point(s) of player and size of this list will be no. of player(s).
player = 0 #This will show the no. of player(s) in game

# This is issnake function
def issnake(noPlayer, rollNo):
    ''' This is a function which takes two input no of player and rolled value after throwing dice and will set current position
of player to appropriate place...if snake is encountere than set value to the tail of snake or if snake is not encountered
then do nothing... '''
    tempPlayerValue = playerList[noPlayer] + rollNo #temporary current position of player
    for i in range(0, len(snakeM)):
        if snakeM[i] == tempPlayerValue: #if snake is encountered
            print ("\t\tYou are encountered with snake's mouth at position ", tempPlayerValue)
            tempPlayerValue = snakeT[i] #replace tempPlayerValue with value at snake's tail
            playerList[noPlayer] = tempPlayerValue #set tempPlayerValue to the real value of player
            print ("\t\tNow...you are at position ", tempPlayerValue)
            return 1 #return 1 if snake is encountered
    return 0 #return 0 if snake is not encountered
#end of snake function
        
#This is isLader function
def isLader(noPlayer, rollNo):
    ''' This is function which takes two input no of player and rolled value after throwing dice and will st current position of player to appropriate place...if base of lader is encountered
than set value to the top of the lader and if no lader's base is encountered than do nothing....'''
    tempPlayerValue = playerList[noPlayer] + rollNo #temporary current position of player
    for i in range(0, len(laderB)):
        if laderB[i] == tempPlayerValue: #if lader base is encountered
            print ("\t\tYou are encountered with lader's base at position ", tempPlayerValue)
            tempPlayerValue = laderT[i] #replace tempPlayerValue with value at lader's top
            playerList[noPlayer] = tempPlayerValue #set tempPlayerValue to the real value of Player
            print ("\t\tNow...you are at position ", tempPlayerValue)
            return 1 #return 1 if lader is encountered
    return 0 #return 0 if lader is not encountered
#end of lader function

#starting of real game of snake and lader
while True:
    try:
        print('Enter no. of player wants to play this game: ')
        player = int(input()) #take input from user for the no. of player(s) in game
        if ((player <= 10) and (player >= 1)): #break while loop if no. of player is between 1 to 10
            break
        elif player <= 0: #show error if player is less than 1
            print ('atleast 1 player is needed to play this game')
        else: #show error if no. of player is greater than 10
            print ('Only 10 player(s) can play at a time.')
    except ValueError: #show error if value is not of int type
        print('Please enter any natural no. entry')
for value in range(0, player): #loop till no. of player(s) in the game
    playerList.append(0) #assign zero to all player(s)
print ('\n\n\t\tWELCOME TO THE GAME.....\n')
while True: #loop till any one player don't reach at 100
    isB = 0 #it will be zero till inner loop is not brake
    for play in range(0, player): #play game for each and every player
        isFinish = 0 #it will set to one if player is at home and  1 is not rolled
        isNormal = 0 #if lader or snake is encountered then it will set to 1
        rolledValue = 0 #initially take dice value to zero
        print('\n\tPLAYER ', play + 1, ': ')
        while True: #wait for player till 'r' is not entered by him/her
            print ("\t\tEnter 'r' to roll dice for player ", play+1, ": ", end = ' ')
            isRoll = input()
            if isRoll == 'r' or isRoll == 'R': #break loop if player enetered 'r'
                break
        rolledValue = random.randint(1, 6) #generating random no. from 1 to 6
        if (playerList[play] == 0) and (rolledValue != 1): #player is at his/her home and 1 is not rolled yet
            print ("\n\t\tYou got: ", rolledValue)
            print ("\t\tYou are at home...you need 1 to get out of it!")
            isFinish = 1 #set variable 1 as player is at home and 1 is not encountered
        if isFinish == 0:
            print ("\n\t\tYou got: ", rolledValue)
            print ("\t\tYou were at position ", playerList[play])
            isNormal = issnake(play, rolledValue)
            if isNormal == 0:
                isNormal = isLader(play, rolledValue)
        if (isFinish == 0) and (isNormal == 0):
            if (playerList[play] + rolledValue) > 100:
                print ("\n\t\tYou got: ", rolledValue)
                print ("\t\tYou need ", 100-playerList[play], " to win this game...")
            else:
                playerList[play] = playerList[play] + rolledValue #change current position of current player
                print ("\t\tNow...You are at position ", playerList[play])
        print ("\n\n\t\tPOSITION OF EVERY PLAYER")
        for every in range(0, len(playerList)):
            print ("PLAYER ", every+1, ": ", playerList[every])
        print("\n\n")
        for every in range(0, len(playerList)):
            if playerList[every] == 100:
                isB = 1 #set isB to 1 to break while loop and inner for loop
        if isB == 1:
            break #break for loop if any player is reached to 100
    if isB==1:
        break #break while loop if any player is reached to 100
#now we found a player who is winner of this game
for every in range(0, len(playerList)):
    if playerList[every] == 100:
        print ("\n\n\n\t\t\tCONGRATULATIONS!")
        print ("\n\tWINNER OF THIS GAME IS   :::::  PLAYER ", every+1)
        break
print ("\n\t\t\tTHANK YOU!\n\nEND OF THE GAME...")
#END OF THE GAME
