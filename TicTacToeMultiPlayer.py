from tkinter import *
from tkinter import messagebox
from functools import partial
import random
from copy import deepcopy

side = 0

global board
board = [[" " for x in range(3)] for y in range(3)]

# for i in range(3):
#     for j in range(3):
#         print(board[i][j])


# Function to return if any side has won or not
def winner(a,k):
    return ((a[0][0] == k and a[0][1] == k and a[0][2] == k) or
    (a[1][0] == k and a[1][1] == k and a[1][2] == k) or
    (a[2][0] == k and a[2][1] == k and a[2][2] == k) or
    (a[0][0] == k and a[1][1] == k and a[2][2] == k) or
    (a[1][2] == k and a[1][1] == k and a[2][0] == k) or
    (a[0][0] == k and a[1][0] == k and a[2][0] == k) or
    (a[0][1] == k and a[1][1] == k and a[2][1] == k) or
    (a[0][2] == k and a[1][2] == k and a[2][2] == k))

# This function regulates the turns for both players
def gettext(i,j,gb,l1,l2):
    global side

    if board[i][j] == ' ':
        if side % 2 == 0:
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)

            board[i][j] = "X"

        else:
            l2.config(state = DISABLED)
            l1.config(state = ACTIVE)

            board[i][j] = "O"

        side = side + 1
        button[i][j].config(text = board[i][j])

        if(winner(board,"X")):
            gb.destroy()

            win = messagebox.showinfo("Winner", "Player 1 has won this match!!!!!")
        
        elif(winner(board,"O")):
            gb.destroy()

            win = messagebox.showinfo("Winner", "Player 2 has won this match!!!!!")

        elif(isfull()):
            gb.destroy()

            win = messagebox.showinfo("Tie", "The match has ended up in a tie")

# This function tells if the board ready to use or not
def free(i,j):
    return board[i][j] == " "

# Returns if the board is completely filled or not
def isfull():
    flag = True

    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag 

def boardgame(game_board,l1,l2):
    global button
    button = []

    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []

        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(gettext,i,j,game_board,l1,l2)
            button[i][j] = Button(game_board,bd = 7,command=get_t,height=5,width=9)
            button[i][j].grid(row=m,column=n)

    game_board.mainloop()

def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        
        corner = []
        
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        
        edge = []
        
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            
            return edge[move]   

def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")

    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)


def gameboard_pc(game_board, l1, l2):
    global button
    
    button = []
    
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)
 
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)
 
 
 
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player 1 : X", width=10)
 
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2 : O",
                width=10, state=DISABLED)
 
    l2.grid(row=2, column=1)
    boardgame(game_board, l1, l2)

def play():
    Kartikey = Tk()
    Kartikey.geometry("400x400")
    Kartikey.title("-----TIC-TAC-TOE-----")

    wpc = partial(withpc, Kartikey)
    wpl = partial(withplayer, Kartikey)
 
    head = Button(Kartikey, text="---Welcome to The Tic-Tac-Toe---",
                  activeforeground='red',
                  activebackground="yellow", bg="white",
                  fg="red",height=4, width=500, font='summer', bd=5)
 
    B1 = Button(Kartikey, text="Single Player", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
 
    B2 = Button(Kartikey, text="Multi Player", command=wpl, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
 
    B3 = Button(Kartikey, text="Exit", command=Kartikey.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    Kartikey.mainloop()

if __name__ == '__main__':
    play()