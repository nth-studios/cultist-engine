def Analyze(boardIn):
    pawnProgressionMultiplier = 0.1
    score = 0
    for y in range(8):
        for x in range(8):
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
                    score -= 1+pawnProgressionMultiplier*y
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
                    score += 1+pawnProgressionMultiplier*(7-y)

    return score

def checkProtected(piece, boardIn, x, y):
    score = 0
    #print("checking protected: ", piece, x, y)
    match piece:
        case "p":
            if(y < 7):
                if x > 0 : score += protectionMultiplier(boardIn[y + 1, x - 1])
                if x < 7 : score += protectionMultiplier(boardIn[y + 1, x + 1])
        case "P":
            if (y > 0):
                if x > 0 : score += protectionMultiplier(boardIn[y - 1, x - 1])
                if x < 7 : score += protectionMultiplier(boardIn[y - 1, x + 1])
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
    if(x=="."):
        return 0
    if(x.isupper()):
        return 1
    return -1

def protectionMultiplier(x):
    multiplier = 0
    match x.lower():
        case "r":
            multiplier = 0.5
        case "n":
            multiplier = 0.3
        case "b":
            multiplier = 0.3
        case "q":
            multiplier = 2
        case "k":
            multiplier = 2
        case "p":
            multiplier = 0.1
    return multiplier*whiteBlack(x)