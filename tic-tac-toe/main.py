#!/usr/bin/python
'''
File: main.py
Project: min-max-implementations/tic-tac-toe
File Created: Tuesday, 24th July 2018 6:50:44 pm
Author: Sujan Poudel (https://github.com/psuzn)
-----
Last Modified: Wednesday, 25th July 2018 11:49:13 am
Modified By: Sujan Poudel 
'''
import tictactoe,pygame,copy
from pygame.locals import *



# draw:game is in draw noone wins
# intermediate: there is/are empty space(s) 
# x is human and y is computer
xWin,oWin,draw,intermediate = range(4)

recuisions = 0;
def minmax(currentGrid,recursionLevel):
    global recuisions
    recuisions+=1
    status = checkStatus(currentGrid)
   # print(f"recursion:{recursionLevel} status:{status},\n{currentGrid}\n")
    if status is xWin:
        return -10
    elif status is oWin :
        return 10
    elif status is draw:
        return 0
    else:
        branches = []
        for i in range(3):
            for j in range(3):
                if currentGrid[i][j] is None:
                    newGrid = copy.deepcopy(currentGrid)
                    if recursionLevel % 2 == 0:
                        newGrid[i][j] = "O"
                    else:
                        newGrid[i][j] = "X"
                    score = minmax(newGrid,recursionLevel+1)
                    branches.append([i,
                                    j,
                                    score])
        max = [None,None,-100]      
        min = [None,None, 100]                 
        for b  in branches:
            if b[2] > max[2]:
                max = b
            if b[2] < min[2]:
                min = b 
        if recursionLevel > 0:
            if recursionLevel % 2 == 0:
                return max[2]
            else:
                return min[2]
        else: # top of the tree always max
            return max[:2]
    
def checkStatus(grid):
    winner = None
        # check for winning rows
    for row in range (0, 3):
        if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
           (grid [row][0] is not None)):
            # this row won
            winner = grid[row][0]
            break

    # check for winning columns
    for col in range (0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            # this column won
            winner = grid[0][col]
            break

    # check for diagonal winners
    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
       (grid[0][0] is not None):
        # game won diagonally left to right
        winner = grid[0][0]

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
       (grid[0][2] is not None):
        # game won diagonally right to left
        winner = grid[0][2]
    emptySpaces = [x for row in grid for x in row if x==None]
    #print(f"winner:{winner}")
    if len(emptySpaces) > 0:
        return intermediate
    elif winner:
        return xWin if winner =="X" else oWin
    else:
        return draw
        
if __name__ =="__main__":
    pygame.init()
    ttt = pygame.display.set_mode ((300, 325))
    pygame.display.set_caption ('Tic-Tac-Toe')

    # create the game board
    board = tictactoe.initBoard (ttt)

    # main event loop
    running = 1

    while (running == 1):
        if tictactoe.XO=="O":
                x,y = minmax(tictactoe.grid,0)
                print(f"recusion was {recuisions}")
                tictactoe.drawMove(board,x,y,"O")
                tictactoe.switchTurn()
                recuisions =0
        for event in pygame.event.get():
            if event.type is QUIT:
                    running = 0
            if tictactoe.XO =="X" and event.type is MOUSEBUTTONDOWN and tictactoe.XO =="X":
                    # the user clicked; place an X or O
                 tictactoe.clickBoard(board)
           
        # check for a winner
        tictactoe.gameWon (board)

        # update the display
        tictactoe.showBoard (ttt, board)

