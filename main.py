import numpy as np

def FENParser(fenparserIn, boardIn):
    index = 0
    index2 = 0
    boardIn = np.full((8, 8), '.')
    for x in fenparserIn:
        match x:
            case "r":
                boardIn[index2, index] = x
                index += 1
            case "n":
                boardIn[index2, index] = x
                index += 1
            case "b":
                boardIn[index2, index] = x
                index += 1
            case "q":
                boardIn[index2, index] = x
                index += 1
            case "k":
                boardIn[index2, index] = x
                index += 1
            case "p":
                boardIn[index2, index] = x
                index += 1
            case "R":
                boardIn[index2, index] = x
                index += 1
            case "N":
                boardIn[index2, index] = x
                index += 1
            case "B":
                boardIn[index2, index] = x
                index += 1
            case "Q":
                boardIn[index2, index] = x
                index += 1
            case "K":
                boardIn[index2, index] = x
                index += 1
            case "P":
                boardIn[index2, index] = x
                index += 1
            case "/":
                index = 0
                index2 += 1
            case "1":
                index += 1
            case "2":
                index += 2
            case "3":
                index += 3
            case "4":
                index += 4
            case "5":
                index += 5
            case "6":
                index += 6
            case "7":
                index += 7
            case "8":
                index += 8
        #print(x, index, index2)

    return boardIn


name = "Cultist"
version = "0.0.1"
print("Welcome to the basic " + name + " engine platform, v" + version + ".\n\n")

board = np.full((8, 8), '.')

FENInput = input("Enter a FEN string for parsing:")

board = FENParser(FENInput, board)

print(board)

