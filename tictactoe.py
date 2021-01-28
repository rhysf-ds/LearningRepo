nought = ("/", "\\", "\\", "/")
cross = ("\\", "/", "/", "\\")
blank = (" ", " ", " ", " ")
boardpositions = ["top left", "top middle", "top right", "middle left", "middle middle", "middle right", "bottom left",
                  "bottom middle", "bottom right"]


def showboard(boardstate):
    print("\
    {0} {1}|{4} {5}|{8} {9}\n\
    {2} {3}|{6} {7}|{10} {11}\n\
    ___|___|___\n\
    {12} {13}|{16} {17}|{20} {21}\n\
    {14} {15}|{18} {19}|{22} {23}\n\
    ___|___|___\n\
    {24} {25}|{28} {29}|{32} {33}\n\
    {26} {27}|{30} {31}|{34} {35}\n\
       |   |  ".format(*boardstate["top left"], *boardstate["top middle"], *boardstate["top right"],
                       *boardstate["middle left"], *boardstate["middle middle"], *boardstate["middle right"],
                       *boardstate["bottom left"], *boardstate["bottom middle"], *boardstate["bottom right"]))


def playerselection():
    player = [""]
    while player not in ["X", "O", ""]:
        player = input("Player 1 do you want to be noughts (O) or crosses(X)?: ")
        if player not in ["X", "O", ""]:
            print("Sorry wrong choice, choose noughts (O) or crosses (X)")
    return player


def movecheck(move, boardstate):
    if move in boardpositions:
        if boardstate[move] == blank:
            return True
    else:
        return False


def makemove(move, player, boardstate):
    if player == ["X"]:
        boardstate[move] = cross
        return boardstate
    else:
        boardstate[move] = nought
        return boardstate


def checkwin(boardstate):
    if boardstate["top left"] == boardstate["top middle"] == boardstate["top right"] \
            and boardstate["top right"] != blank:
        return True
    if boardstate["middle left"] == boardstate["middle middle"] == boardstate["middle right"] \
            and boardstate["middle right"] != blank:
        return True
    if boardstate["bottom left"] == boardstate["bottom middle"] == boardstate["bottom right"] \
            and boardstate["bottom right"] != blank:
        return True
    if boardstate["top left"] == boardstate["middle middle"] == boardstate["bottom right"] \
            and boardstate["bottom right"] != blank:
        return True
    if boardstate["bottom left"] == boardstate["middle middle"] == boardstate["top right"] \
            and boardstate["top right"] != blank:
        return True
    if boardstate["top left"] == boardstate["middle left"] == boardstate["bottom left"] \
            and boardstate["bottom left"] != blank:
        return True
    if boardstate["top middle"] == boardstate["middle middle"] == boardstate["bottom middle"] \
            and boardstate["bottom middle"] != blank:
        return True
    if boardstate["top right"] == boardstate["middle right"] == boardstate["bottom right"] \
            and boardstate["bottom right"] != blank:
        return True
    else:
        return False


def tictactoe():
    boardstate = {"top left": blank, "top middle": blank, "top right": blank, "middle left": blank,
                  "middle middle": blank, "middle right": blank, "bottom left": blank, "bottom middle": blank,
                  "bottom right": blank}
    winstate = False
    player1 = [""]
    player2 = []
    validmove = False
    currentturn = 0
    ""
    while not winstate:
        while not validmove:
            while player1 == [""]:
                player1 = playerselection()
                if player1 == ["X"]:
                    player2 = ["O"]
                else:
                    player2 = ["X"]
            if currentturn in [0, 2, 4, 6, 8]:
                playerturn = "player 1"
                player = player1
            else:
                playerturn = "player 2"
                player = player2
            move = input(
                "What position do you want to play {}? use top/middle/bottom left/middle/right (top left/ middle "
                "middle): ".format(
                    playerturn))
            if movecheck(move.lower(), boardstate):
                boardstate = makemove(move, player, boardstate)
                showboard(boardstate)
                if checkwin(boardstate):
                    winstate = True
                    print(f"Well done {playerturn} you won!")
                    break
                elif currentturn == 8:
                    print("It's a tie!")
                    winstate = True
                    break
                currentturn += 1
            else:
                print("invalid move try again")


def play():
    keepon = "yes"
    while keepon.lower() == "yes":
        tictactoe()
        keepon = input("Play again? yes/no")


play()
