def Analyze(boardIn):
    score = 0
    for x in range(8):
        for y in range(8):
            checkSquare = boardIn[y, x]
            score += checkProtected(checkSquare, boardIn, x, y)
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

def checkProtected(piece, boardIn, x, y):
    score = 0
    print("checking protected: ", piece, x, y)
    # match x:
    #     case "r":
    #         if()
    #     case "n":
    #         score -= 4
    #     case "b":
    #         score -= 4
    #     case "q":
    #         score -= 10
    #     case "k":
    #         score += 0
    #     case "p":
    #         score -= 1
    #     case "R":
    #         score += 5
    #     case "N":
    #         score += 4
    #     case "B":
    #         score += 4
    #     case "Q":
    #         score += 10
    #     case "K":
    #         score += 0
    #     case "P":
    #         score += 1
    return score

def whiteBlack(x):
    if(x.isUpper()):
        return True
    return False