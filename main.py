import numpy as np
import FEN
import GameAnalyzer

WHITE = 1
EMPTY = 0
BLACK = -1


name = "Cultist"
version = "0.0.1"
print("Welcome to the basic " + name + " engine platform, v" + version + ".\n\n")
playingAs = BLACK

board = np.full((8, 8), '.')

while True:

    FENInput = input("\nEnter a FEN string for parsing:")

    board, options = FEN.FENParser(FENInput, board)

    turnBW = options[0]
    castling = options[1]
    enPassantSquare = options[2]
    halfMoveClock = int(options[3])
    fullMove = int(options[4])

    print(board)

    # print(board)
    print("Side to move: ", turnBW.upper())
    print("Move number: ", fullMove)

    if playingAs == WHITE:
        print("\nYour best move as white would be: ")
        print(GameAnalyzer.getBestMove(board, WHITE, printEnable=True, depth=1))
    else:
        print("\nYour best move as black would be: ")
        print(GameAnalyzer.getBestMove(board, BLACK, printEnable=True, depth=1))

# moveList, APArray = GameAnalyzer.moveAnalyzer(board)
#
# # print("Attacked Array: ")
# # print(APArray[0])
# # print("Attacking Array: ")
# # print(APArray[1])
# # print("Protected Array: ")
# # print(APArray[2])
# # print("Protecting Array: ")
# # print(APArray[3])
#
# moveListW = []
# moveListB = []
# for i in moveList:
#     if i.wB == 1:
#         moveListW.append(i.__str__())
#     else:
#         moveListB.append(i.__str__())
#
# print("\nWhite moves:")
# print(moveListW)
# print("\nBlack moves:")
# print(moveListB)
# # print("\n\nProtect Matrix")
# # print(protected)
# # print("\n\nAttack Matrix")
# # print(attacked)
#
# currScore, whiteChecked, blackChecked = GameAnalyzer.scoreAnalyzer(board, APArray, moveList)
# print("\nCurrent analysis: ", round(currScore, 3))
# print("Check status [White]:", whiteChecked)
# print("Check status [Black]:", blackChecked)
#
# bestMove = ""
# bestScore = -1000
#
# for moveCheck in moveList:
#     if moveCheck.wB == WHITE:
#         newBoard = GameAnalyzer.alterBoardForMove(moveCheck, board)
#         newMovelist, newAP = GameAnalyzer.moveAnalyzer(newBoard)
#         newScore, newWC, newBC = GameAnalyzer.scoreAnalyzer(newBoard, newAP, newMovelist)
#         print(moveCheck, np.round(newScore, 3), newWC)
#         if whiteChecked:
#             if not newWC:
#                 if newScore > bestScore:
#                     bestScore = newScore
#                     bestMove = moveCheck
#         else:
#             if newScore > bestScore:
#                 bestScore = newScore
#                 bestMove = moveCheck
#
# if bestScore == -1000:
#     print("You have no available moves, and have lost the game!")
# else:
#     print("\nYour best is: ")
#     print(bestMove)
#     print(" with a score of ")
#     print(bestScore)
