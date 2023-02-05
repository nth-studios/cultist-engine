import numpy as np
import FEN
import GameAnalyzer

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

moveListW, moveListB, attacked, protected = GameAnalyzer.moveAnalyzer(board)

print("\nWhite moves:")
print(moveListW)
print("\nBlack moves:")
print(moveListB)
print("\n\nProtect Matrix")
print(protected)
print("\n\nAttack Matrix")
print(attacked)

currScore = GameAnalyzer.scoreAnalyzer(board, attacked, protected, len(moveListW), len(moveListB))
print("Current analysis: ", round(currScore, 3))

