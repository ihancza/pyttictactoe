fieldtopos = {"a1": 0, "b1": 1, "c1": 2, "a2": 3, "b2": 4, "c2": 5, "a3": 6, "b3": 7, "c3": 8}
postogui = {0: "O", 1: "X", 2: "-"}
winpos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
gstatus = True

def startgame():
    global pos
    global player
    pos = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    player = 0


def endgame():
    board()
    global gstatus
    gstatus = False


def chfield(a, b):
    turn = fieldtopos[input("Choose the field (ex. a1): ")]
    if pos[turn] == 2:
        pos[turn] = a
        global player
        player = b
    else:
        print("Choose blank one")


def board():
    print("   a     b     c\n      |     |     \n1  {}  |  {}  |  {}  \n _____|_____|_____\n      |     |     \n2  {}  |  {}  |  {}  \n _____|_____|_____\n      |     |     \n3  {}  |  {}  |  {}  \n      |     |     ".format(postogui[pos[0]], postogui[pos[1]], postogui[pos[2]], postogui[pos[3]], postogui[pos[4]], postogui[pos[5]],postogui[pos[6]], postogui[pos[7]], postogui[pos[8]]))


def game():
    global fieldtopos
    global pos
    global postogui
    global player
    global winpos
    global gstatus
    startgame()
    while gstatus:
        board()
        if player == 0:
            print("Circle turn")
            chfield(0, 1)
        else:
            print("Cross turn")
            chfield(1, 0)
        for wpos in winpos:
            if pos[wpos[0]] == pos[wpos[1]] and pos[wpos[1]] == pos[wpos[2]] and pos[wpos[1]] != 2:
                if player == 1:
                    endgame()
                    print("Circle won")
                else:
                    endgame()
                    print("Cross won")
            else:
                if not 2 in pos:
                    endgame()
                    print("Draw")
                else:
                    continue


while True:
    game()
    if input("Wanna play again?(y, n)") == "y":
        gstatus = True
        game()
    else:
        break
