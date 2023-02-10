import numpy as np
import FEN
import GameAnalyzer

flagStart = False
while not flagStart:
    uciCheck = input()
    if uciCheck == "uci":
        flagStart = True

print("id name Cultist Engine")
print("id author Nicholas Brigando")

print("uciok")


flagStart = False
while not flagStart:
    uciCheck = input()
    if uciCheck == "isready":
        flagStart = True

print("readyok")

flagStart = False
while not flagStart:
    uciCheck = input()
    if uciCheck == "ucinewgame":
        flagStart = True

flagQuit = False
while not flagQuit:

    inData = input()
    if inData == "isready":
        print("info isready recieved")
        inData = input()

    gameData = inData.split(" ")
    board = np.full((8, 8), '.')
    if(gameData[1] == "startpos"):
        board, options = FEN.FENParser(FEN.STARTPOS, board)
    else:
        board, options = FEN.FENParser(gameData[1], board)

    colour = GameAnalyzer.WHITE



    if len(gameData) > 2:
        if len(gameData) % 2 == 0:
            colour = GameAnalyzer.BLACK
        for i in range(3, len(gameData)):
            #print("info iterator: ", i, gameData[i])
            nextMove = GameAnalyzer.convertNotationToCoords(gameData[i])
            nextMoveType = GameAnalyzer.Move(nextMove[0], nextMove[1], nextMove[2], nextMove[3], colour)
            board = GameAnalyzer.alterBoardForMove(nextMoveType, board)


    #print("info I am ", "white" if colour == 1 else "black")


    flagStart = False
    while not flagStart:
        uciCheck = input().split(" ")
        if uciCheck[0] == "go":
            flagStart = True

    bestMove = GameAnalyzer.getBestMove(board, colour, False, 1)
    print("bestmove ", bestMove)
