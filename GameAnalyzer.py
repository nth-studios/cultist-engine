import struct

import numpy as np

class Move:
    def __init__(self, xo: int, yo: int, xn: int, yn: int, wB: int):
        self.xo = xo
        self.yo = yo
        self.xn = xn
        self.yn = yn
        self.wB = wB

    def __str__(self):
        return convertCoordsToNotation(self.xo, self.yo, self.xn, self.yn)



def moveAnalyzer(boardIn):
    protected = np.full((8, 8), 0.0)
    attacked = np.full((8, 8), 0.0)
    moveList = []
    for y in range(8):
        for x in range(8):
            checkSquare = boardIn[y, x]
            wBo = whiteBlack(checkSquare)
            match checkSquare:
                case "q" | "Q":
                    if y < 7 and x < 7:
                        xn = x + 1
                        yn = y + 1
                        while xn < 8 and yn < 8:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn += 1
                            yn += 1
                    if y > 0 and x < 7:
                        xn = x + 1
                        yn = y - 1
                        while xn < 8 and yn >= 0:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn += 1
                            yn -= 1
                    if y < 7 and x > 0:
                        xn = x - 1
                        yn = y + 1
                        while xn >= 0 and yn < 8:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn -= 1
                            yn += 1
                    if y > 0 and x > 0:
                        xn = x - 1
                        yn = y - 1
                        while xn >= 0 and yn >= 0:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn -= 1
                            yn -= 1
                    if y < 7:
                        for i in range(y + 1, 8, 1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x, i, wBo))
                                attacked[i, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if y > 0:
                        for i in range(y - 1, -1, -1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x, i, wBo))
                                attacked[i, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if x < 7:
                        for i in range(x + 1, 8, 1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, i] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))
                    if x > 0:
                        for i in range(x - 1, -1, -1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))

                case "k" | "K":
                    if y < 7 and x < 7:
                        xn = x + 1
                        yn = y + 1
                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y > 0 and x < 7:
                        xn = x + 1
                        yn = y - 1
                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y < 7 and x > 0:
                        xn = x - 1
                        yn = y + 1

                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y > 0 and x > 0:
                        xn = x - 1
                        yn = y - 1
                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y < 7:
                        i = y + 1
                        wBn = whiteBlack(boardIn[i, x])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, x, i, wBo))
                            attacked[i, x] += attackMultiplier(boardIn[i, x])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[i, x])
                        else:
                            moveList.append(Move(x, y, x, i, wBo))
                    if y > 0:
                        i = y - 1
                        wBn = whiteBlack(boardIn[i, x])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, x, i, wBo))
                            attacked[i, x] += attackMultiplier(boardIn[i, x])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[i, x])
                        else:
                            moveList.append(Move(x, y, x, i, wBo))
                    if x < 7:
                        i = x + 1
                        wBn = whiteBlack(boardIn[y, i])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, i, y, wBo))
                            attacked[y, i] += attackMultiplier(boardIn[y, i])
                        elif wBn == wBo:
                            protected[y, i] += protectionMultiplier(boardIn[y, i])
                        else:
                            moveList.append(Move(x, y, i, y, wBo))
                    if x > 0:
                        i = x - 1
                        wBn = whiteBlack(boardIn[y, i])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, i, y, wBo))
                            attacked[y, i] += attackMultiplier(boardIn[y, i])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[y, i])
                        else:
                            moveList.append(Move(x, y, i, y, wBo))

                case "b" | "B":
                    if y < 7 and x < 7:
                        xn = x + 1
                        yn = y + 1
                        while xn < 8 and yn < 8:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn += 1
                            yn += 1
                    if y > 0 and x < 7:
                        xn = x + 1
                        yn = y - 1
                        while xn < 8 and yn >= 0:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn += 1
                            yn -= 1
                    if y < 7 and x > 0:
                        xn = x - 1
                        yn = y + 1
                        while xn >= 0 and yn < 8:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn -= 1
                            yn += 1
                    if y > 0 and x > 0:
                        xn = x - 1
                        yn = y - 1
                        while xn >= 0 and yn >= 0:
                            wBn = whiteBlack(boardIn[yn, xn])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, xn, yn, wBo))
                                attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[yn, xn])
                                break
                            else:
                                moveList.append(Move(x, y, xn, yn, wBo))
                            xn -= 1
                            yn -= 1

                case "r" | "R":
                    if y < 7:
                        for i in range(y + 1, 8, 1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x, i, wBo))
                                attacked[i, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if y > 0:
                        for i in range(y - 1, -1, -1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x, i, wBo))
                                attacked[i, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if x < 7:
                        for i in range(x + 1, 8, 1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, i] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))
                    if x > 0:
                        for i in range(x - 1, -1, -1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))

                case "n" | "N":
                    xs = []
                    ys = []
                    if x > 1 and y < 7:  # 2 left, 1 down
                        xs.append(x-2)
                        ys.append(y+1)
                    if x > 1 and y > 0:  # 2 left, 1 up
                        xs.append(x-2)
                        ys.append(y-1)
                    if x > 0 and y < 6:  # 1 left, 2 down
                        xs.append(x-1)
                        ys.append(y+2)
                    if x > 0 and y > 1:  # 1 left, 2 up
                        xs.append(x-1)
                        ys.append(y-2)
                    if x < 6 and y < 7:  # 2 right, 1 down
                        xs.append(x+2)
                        ys.append(y+1)
                    if x < 6 and y > 0:  # 2 right, 1 up
                        xs.append(x+2)
                        ys.append(y-1)
                    if x < 7 and y < 6:  # 1 right, 2 down
                        xs.append(x+1)
                        ys.append(y+2)
                    if x < 7 and y > 1:  # 1 right, 2 up
                        xs.append(x+1)
                        ys.append(y-2)
                    for i in range(len(xs)):
                        wBn = whiteBlack(boardIn[ys[i], xs[i]])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xs[i], ys[i], wBo))
                            attacked[ys[i], xs[i]] += attackMultiplier(boardIn[ys[i], xs[i]])
                        elif wBn == wBo:
                            protected[y, x] += protectionMultiplier(boardIn[ys[i], xs[i]])
                        else:
                            moveList.append(Move(x, y, xs[i], ys[i], wBo))

                case "p":
                    if y < 7:
                        if whiteBlack(boardIn[y + 1, x]) == 0:
                            moveList.append(Move(x, y, x, y + 1, wBo))
                        if x > 0:
                            wBn = whiteBlack(boardIn[y + 1, x - 1])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x - 1, y + 1, wBo))
                                attacked[y + 1, x - 1] += attackMultiplier(boardIn[y + 1, x - 1])
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y + 1, x - 1])
                        if x < 7:
                            wBn = whiteBlack(boardIn[y + 1, x + 1])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x + 1, y + 1, wBo))
                                attacked[y + 1, x + 1] += attackMultiplier(boardIn[y + 1, x + 1])
                            elif wBn == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y + 1, x + 1])

                case "P":
                    if y > 0:
                        if whiteBlack(boardIn[y - 1, x]) == 0:
                            moveList.append(Move(x, y, x, y - 1, wBo))
                        if x > 0:
                            wB = whiteBlack(boardIn[y - 1, x - 1])
                            if wB == -1 * wBo:
                                moveList.append(Move(x, y, x - 1, y - 1, wBo))
                                attacked[y - 1, x - 1] += attackMultiplier(boardIn[y - 1, x - 1])
                            elif wB == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y - 1, x - 1])
                        if x < 7:
                            wB = whiteBlack(boardIn[y - 1, x + 1])
                            if wB == -1 * wBo:
                                moveList.append(Move(x, y, x + 1, y - 1, wBo))
                                attacked[y - 1, x + 1] += attackMultiplier(boardIn[y - 1, x + 1])
                            elif wB == wBo:
                                protected[y, x] += protectionMultiplier(boardIn[y - 1, x + 1])

    return moveList, attacked, protected


def scoreAnalyzer(boardIn, attackedIn, protectedIn, moveListIn):
    pawnProgressionMultiplier = 0.1
    score = 0
    for y in range(8):
        for x in range(8):
            checkSquare = boardIn[y, x]
            match checkSquare:
                case "r":
                    score -= (5 - attackedIn[y, x] + protectedIn[y, x])
                case "n":
                    score -= (4 - attackedIn[y, x] + protectedIn[y, x])
                case "b":
                    score -= (4 - attackedIn[y, x] + protectedIn[y, x])
                case "q":
                    score -= (10 - attackedIn[y, x] + protectedIn[y, x])
                case "k":
                    score += (0 - attackedIn[y, x] + protectedIn[y, x])
                case "p":
                    score -= (1 + pawnProgressionMultiplier * y - attackedIn[y, x] + protectedIn[y, x])
                case "R":
                    score += (5 - attackedIn[y, x] + protectedIn[y, x])
                case "N":
                    score += (4 - attackedIn[y, x] + protectedIn[y, x])
                case "B":
                    score += (4 - attackedIn[y, x] + protectedIn[y, x])
                case "Q":
                    score += (10 - attackedIn[y, x] + protectedIn[y, x])
                case "K":
                    score += (0 - attackedIn[y, x] + protectedIn[y, x])
                case "P":
                    score += (1 + pawnProgressionMultiplier * (7 - y) - attackedIn[y, x] + protectedIn[y, x])
    return score


def checkProtected(protectedIn, x, y):
    score = 0
    score += protectionMultiplier(protectedIn[y + 1, x - 1])
    return score


def whiteBlack(x):
    if x == ".":
        return 0
    if x.isupper():
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


def attackMultiplier(x):
    multiplier = 0
    match x.lower():
        case "r":
            multiplier = 4
        case "n":
            multiplier = 3
        case "b":
            multiplier = 3
        case "q":
            multiplier = 10
        case "k":
            multiplier = 10
        case "p":
            multiplier = 0.1
    return multiplier


def convertCoordsToNotation(xo, yo, xn, yn):
    notation = str(chr(xo + 97)) + str((8 - yo)) + str(chr(xn + 97)) + str((8 - yn))
    return notation
