from os import system, name


def createBoard():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def checkWin(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    if emptySpaces == False:
        print("Tie game\n")
        return "Tie"
    return False


def emptySpaces(board):
    spaces = 9
    for row in range(3):
        for column in range(3):
            if board[row][column] != " ":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def displayBoard(board):
    rows = len(board)
    clearScreen()
    print("---+---+---")
    for i in range(rows):
        print(board[i][0], " |", board[i][1], "|", board[i][2])
        print("---+---+---")
    return


def gameProcess(turnNum, board, player1, player2):
    if turnNum % 2 == 0:
        currentPlayer = player1
    else:
        currentPlayer = player2
    print("Player %s, it is your turn\n" % currentPlayer)
    position = choosePosition(board)
    if emptySpaces(board) == True:
        placeMove(board, position, currentPlayer)
        clearScreen()
    else:
        print("Tie game!\n")
    return


def choosePosition(board):
    row = -1
    column = -1
    while int(row) not in [0, 1, 2] or int(column) not in [0, 1, 2]:
        row = input(
            "Pick a row:"
            "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"
        )

        column = input(
            "Pick a column:"
            "[left column: enter 0, middle column: enter 1, right column enter 2]"
        )
        if int(row) not in [0, 1, 2] or int(column) not in [0, 1, 2]:
            print("Illegal position! Row and Column numbers must be between 0 - 2\n\n")
        elif checkMove(board, row, column) == False:
            row = -1
            column = -1
    row = int(row)
    column = int(column)
    return (row, column)


def checkMove(board, row, column):
    if board[int(row)][int(column)] != " ":
        print("Position occupied, please choose a new move.\n")
        return False
    return True


def placeMove(board, position, currentPlayer):
    board[position[0]][position[1]] = currentPlayer
    return


def choosePlayer():
    player1 = " "
    player2 = " "
    while player1 != "X" and player1 != "O":
        player1 = input("Player 1, choose your symbol: X or O\n")
        if player1 not in ["X", "O"]:
            print("You can only choose between X and O \n")
        elif player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
    return (player1, player2)


def clearScreen():
    system("cls" if name == "nt" else "clear")
    return


def main():
    turnCount = 0
    win = False
    board = createBoard()
    displayBoard(board)
    playerSynmbols = choosePlayer()
    while win == False:
        gameProcess(turnCount, board, playerSynmbols[0], playerSynmbols[1])
        win = checkWin(board)
        displayBoard(board)
        turnCount += 1
    print("####\nGAME OVER\n####\n")
    return


main()
