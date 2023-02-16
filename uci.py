import numpy as np
import FEN
import GameAnalyzer

stateMachine = 0
board = np.full((8, 8), '.')
colour = GameAnalyzer.WHITE

while(True):
    uciInput = input()
    match uciInput:
        case "uci":
            stateMachine = 1
            print("info uci received")

            print("id name Cultist Engine")
            print("id author Nicholas Brigando")

            print("uciok")
        case "isready":
            if stateMachine!=3:
                stateMachine = 2
                print("readyok")

            print("info isready received")

        case "ucinewgame":
            stateMachine = 3
            board = np.full((8, 8), '.')
            print("info isready received")

        case other:
            if stateMachine == 3:
                gameData = uciInput.split(" ")
                board = np.full((8, 8), '.')
                if (gameData[1] == "startpos"):
                    board, options = FEN.FENParser(FEN.STARTPOS, board)
                else:
                    board, options = FEN.FENParser(gameData[1], board)

                colour = GameAnalyzer.WHITE

                if len(gameData) > 2:
                    if len(gameData) % 2 == 0:
                        colour = GameAnalyzer.BLACK
                    for i in range(3, len(gameData)):
                        # print("info iterator: ", i, gameData[i])
                        nextMove = GameAnalyzer.convertNotationToCoords(gameData[i])
                        nextMoveType = GameAnalyzer.Move(nextMove[0], nextMove[1], nextMove[2], nextMove[3], colour)
                        board = GameAnalyzer.alterBoardForMove(nextMoveType, board)
                stateMachine = 4

            elif stateMachine == 4:
                uciCheck = uciInput.split(" ")
                if uciCheck[0] == "go":
                    bestMove, bestScore, avgScore = GameAnalyzer.getBestMove(board, colour, False, 3)
                    print("bestmove ", bestMove)
                    print("info score cp ", bestScore)
                stateMachine = 3
