import tkinter #tl-interface (graphical user interface library)

turns = 0
game_over=False
def set_tile(row,column):
    global current_player,turns

    if(game_over):
        return
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = current_player
    if current_player == player2:
        current_player = player1
    else:
        current_player = player2
    label["text"] = current_player+"'s turn"

    check_winner()
def check_winner():
    global turns, game_over
    turns += 1
#row
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " Wins!", foreground=colour_purple)
            for column in range(3):
                board[row][column].config(foreground=colour_purple, background=colour_white)
            game_over = True
            return
#column
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            label.config(text=board[column][0]["text"] + " Wins!", foreground=colour_purple)
            for row in range(3):
                board[row][column].config(foreground=colour_purple, background=colour_white)
            game_over = True
            return
#diagonals
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " wins!", foreground=colour_purple)
        for i in range(3):
            board[i][i].config(foreground=colour_purple, background=colour_white)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " wins!", foreground=colour_purple)
        board[0][2].config(foreground=colour_purple, background=colour_white)
        board[1][1].config(foreground=colour_purple, background=colour_white)
        board[2][0].config(foreground=colour_purple, background=colour_white)
        game_over = True
        return
#draw
if (turns == 9):
    game_over = True
    label.config(text="Draw!", foreground=colour_purple)

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=current_player+"'s turn", foreground=colour_white)
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground= colour_red, background=colour_black)




#game setup
player1 = "X"
player2 = "O"
current_player = player1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

colour_red = "#FF0000"
colour_purple = "#800080"
colour_black = "#000000"
colour_white = "#FFFFFF"

turns = 0
game_over = False

#Window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player+"'s turn", font=("consolas", 20), background=colour_black,
foreground="White")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas",50,"bold"),
                                            background=colour_black, foreground=colour_red, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("consolas", 20), background=colour_black, foreground=colour_white,
                        command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#centre
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()