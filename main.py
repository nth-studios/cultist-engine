import numpy as np
import FEN as FEN

def scoreAnalyzer(boardIn):
    score = 0

    for x in range(8):
        for y in range(8):
            checkSquare = boardIn[y, x]
            match checkSquare:
                case "r":
                    score -= 5
                case "n":
                    score -= 4
                case "b":
                    score -= 4
                case "q":
                    score -= 10
                case "k":
                    score += 0
                case "p":
                    score -= 1
                case "R":
                    score += 5
                case "N":
                    score += 4
                case "B":
                    score += 4
                case "Q":
                    score += 10
                case "K":
                    score += 0
                case "P":
                    score += 1

    return score

name = "Cultist"
version = "0.0.1"
print("Welcome to the basic " + name + " engine platform, v" + version + ".\n\n")

board = np.full((8, 8), '.')

FENInput = input("Enter a FEN string for parsing:")

board, options = FEN.FENParser(FENInput, board)

turnBW = options[0]
castling = options[1]
enPassantSquare = options[2]
halfMoveClock = int(options[3])
fullMove = int(options[4])

print(board)
print("Side to move: ", turnBW.upper())
print("Move number: ", fullMove)

currScore = scoreAnalyzer(board)
print("Current analysis: ", currScore)

