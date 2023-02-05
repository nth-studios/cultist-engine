import numpy as np

def moveAnalyzer(boardIn):
    protected = np.full((8, 8), 0.0)
    attacked = np.full((8, 8), 0.0)
    moveListW = []
    moveListB = []
    for y in range(8):
        for x in range(8):
            checkSquare = boardIn[y, x]
            match checkSquare:
                case "r":
                    wBo = whiteBlack(checkSquare)
                    if (y < 7):
                        for i in range(y + 1, 8, 1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn==-1*wBo:
                                moveListB.append(convertCoordsToNotation(x, y, x, i))
                                attacked[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            elif wBn==wBo:
                                protected[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveListB.append(convertCoordsToNotation(x, y, x, i))
                    if (y > 0):
                        for i in range(y - 1, -1, -1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveListB.append(convertCoordsToNotation(x, y, x, i))
                                attacked[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveListB.append(convertCoordsToNotation(x, y, x, i))
                    if (x < 7):
                        for i in range(x + 1, 8, 1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveListB.append(convertCoordsToNotation(x, y, i, y))
                                attacked[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveListB.append(convertCoordsToNotation(x, y, i, y))
                    if (x > 0):
                        for i in range(x - 1, -1, -1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveListB.append(convertCoordsToNotation(x, y, i, y))
                                attacked[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveListB.append(convertCoordsToNotation(x, y, i, y))

                # case "n":
                # case "b":
                # case "q":
                # case "k":
                case "p":
                    wBo = whiteBlack(checkSquare)
                    if y < 7:
                        if whiteBlack(boardIn[y + 1, x])==0:
                            moveListB.append(convertCoordsToNotation(x, y, x, y+1))
                        if x>0:
                            wBn = whiteBlack(boardIn[y + 1, x - 1])
                            if wBn==-1*wBo:
                                moveListB.append(convertCoordsToNotation(x, y, x-1, y+1))
                                attacked[y, x] += protectionMultiplier(boardIn[y+1, x-1])
                            elif wBn==wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y+1, x-1])
                        if x<7:
                            wBn = whiteBlack(boardIn[y + 1, x + 1])
                            if wBn==-1*wBo:
                                moveListB.append(convertCoordsToNotation(x, y, x+1, y+1))
                                attacked[y, x] += protectionMultiplier(boardIn[y+1, x+1])
                            elif wBn==wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y+1, x+1])
                # case "R":
                # case "N":
                # case "B":
                # case "Q":
                # case "K":
                case "P":
                    wBo = whiteBlack(checkSquare)
                    if y > 0:
                        if whiteBlack(boardIn[y - 1, x]) == 0:
                            moveListW.append(convertCoordsToNotation(x, y, x, y - 1))
                        if x > 0:
                            wB = whiteBlack(boardIn[y - 1, x - 1])
                            if wB == -1*wBo:
                                moveListW.append(convertCoordsToNotation(x, y, x - 1, y - 1))
                                attacked[y, x] += protectionMultiplier(boardIn[y - 1, x - 1])
                            elif wB == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y - 1, x - 1])
                        if x < 7:
                            wB = whiteBlack(boardIn[y - 1, x + 1])
                            if wB == -1*wBo:
                                moveListW.append(convertCoordsToNotation(x, y, x + 1, y - 1))
                                attacked[y, x] += protectionMultiplier(boardIn[y - 1, x + 1])
                            elif wB == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y - 1, x + 1])

    return moveListW, moveListB, attacked, protected

def scoreAnalyzer(boardIn, attackedIn, protectedIn, numW, numB):
    pawnProgressionMultiplier = 0.1
    score = 0
    for y in range(8):
        for x in range(8):
            checkSquare = boardIn[y, x]
            score += checkProtected(protectedIn, x, y)
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
                    score -= 1 + pawnProgressionMultiplier * y
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
                    score += 1 + pawnProgressionMultiplier * (7 - y)

def checkProtected(protectedIn, x, y):
    score = 0
    score += protectionMultiplier(protectedIn[y + 1, x - 1])
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
            multiplier = 10
        case "p":
            multiplier = 0.1
    return multiplier

def convertCoordsToNotation(xo, yo, xn, yn):
    notation=str(chr(xo+97)) + str((8-yo)) + str(chr(xn+97)) + str((8-yn))
    return notation