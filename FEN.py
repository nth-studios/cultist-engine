import numpy as np


STARTPOS = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def FENParser(fenparserIn, boardIn):
    index = 0
    index2 = 0
    boardIn = np.full((8, 8), '.')
    parser = fenparserIn.split(" ")
    options = parser[1::]
    for x in parser[0]:
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

    return boardIn, options
