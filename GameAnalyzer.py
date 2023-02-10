import numpy as np


WHITE = 1
EMPTY = 0
BLACK = -1



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
    protecting = np.full((8, 8), 0.0)
    attacked = np.full((8, 8), 0.0)
    attacking = np.full((8, 8), 0.0)
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[i, x] += protectionMultiplier(boardIn[i, x])
                                protecting[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if y > 0:
                        for i in range(y - 1, -1, -1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x, i, wBo))
                                attacked[i, x] += attackMultiplier(boardIn[i, x])
                                attacking[y, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[i, x] += protectionMultiplier(boardIn[i, x])
                                protecting[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if x < 7:
                        for i in range(x + 1, 8, 1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                attacking[y, x] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, i] += protectionMultiplier(boardIn[y, i])
                                protecting[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))
                    if x > 0:
                        for i in range(x - 1, -1, -1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                attacking[y, x] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, i] += protectionMultiplier(boardIn[y, i])
                                protecting[y, x] += protectionMultiplier(boardIn[y, i])
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
                            attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                            protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y > 0 and x < 7:
                        xn = x + 1
                        yn = y - 1
                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                            attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                            protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y < 7 and x > 0:
                        xn = x - 1
                        yn = y + 1

                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                            attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                            protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y > 0 and x > 0:
                        xn = x - 1
                        yn = y - 1
                        wBn = whiteBlack(boardIn[yn, xn])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xn, yn, wBo))
                            attacked[yn, xn] += attackMultiplier(boardIn[yn, xn])
                            attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                        elif wBn == wBo:
                            protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                            protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
                        else:
                            moveList.append(Move(x, y, xn, yn, wBo))
                    if y < 7:
                        i = y + 1
                        wBn = whiteBlack(boardIn[i, x])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, x, i, wBo))
                            attacked[i, x] += attackMultiplier(boardIn[i, x])
                            attacking[y, x] += attackMultiplier(boardIn[i, x])
                        elif wBn == wBo:
                            protected[i, x] += protectionMultiplier(boardIn[i, x])
                            protecting[y, x] += protectionMultiplier(boardIn[i, x])
                        else:
                            moveList.append(Move(x, y, x, i, wBo))
                    if y > 0:
                        i = y - 1
                        wBn = whiteBlack(boardIn[i, x])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, x, i, wBo))
                            attacked[i, x] += attackMultiplier(boardIn[i, x])
                            attacking[y, x] += attackMultiplier(boardIn[i, x])
                        elif wBn == wBo:
                            protected[i, x] += protectionMultiplier(boardIn[i, x])
                            protecting[y, x] += protectionMultiplier(boardIn[i, x])
                        else:
                            moveList.append(Move(x, y, x, i, wBo))
                    if x < 7:
                        i = x + 1
                        wBn = whiteBlack(boardIn[y, i])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, i, y, wBo))
                            attacked[y, i] += attackMultiplier(boardIn[y, i])
                            attacking[y, x] += attackMultiplier(boardIn[y, i])
                        elif wBn == wBo:
                            protected[y, i] += protectionMultiplier(boardIn[y, i])
                            protecting[y, x] += protectionMultiplier(boardIn[y, i])
                        else:
                            moveList.append(Move(x, y, i, y, wBo))
                    if x > 0:
                        i = x - 1
                        wBn = whiteBlack(boardIn[y, i])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, i, y, wBo))
                            attacked[y, i] += attackMultiplier(boardIn[y, i])
                            attacking[y, x] += attackMultiplier(boardIn[y, i])
                        elif wBn == wBo:
                            protected[y, i] += protectionMultiplier(boardIn[y, i])
                            protecting[y, x] += protectionMultiplier(boardIn[y, i])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[yn, xn])
                                break
                            elif wBn == wBo:
                                protected[yn, xn] += protectionMultiplier(boardIn[yn, xn])
                                protecting[y, x] += protectionMultiplier(boardIn[yn, xn])
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
                                attacking[y, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[i, x] += protectionMultiplier(boardIn[i, x])
                                protecting[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if y > 0:
                        for i in range(y - 1, -1, -1):
                            wBn = whiteBlack(boardIn[i, x])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x, i, wBo))
                                attacked[i, x] += attackMultiplier(boardIn[i, x])
                                attacking[y, x] += attackMultiplier(boardIn[i, x])
                                break
                            elif wBn == wBo:
                                protected[i, x] += protectionMultiplier(boardIn[i, x])
                                protecting[y, x] += protectionMultiplier(boardIn[i, x])
                                break
                            else:
                                moveList.append(Move(x, y, x, i, wBo))
                    if x < 7:
                        for i in range(x + 1, 8, 1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                attacking[y, x] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, i] += protectionMultiplier(boardIn[y, i])
                                protecting[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))
                    if x > 0:
                        for i in range(x - 1, -1, -1):
                            wBn = whiteBlack(boardIn[y, i])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, i, y, wBo))
                                attacked[y, i] += attackMultiplier(boardIn[y, i])
                                attacking[y, x] += attackMultiplier(boardIn[y, i])
                                break
                            elif wBn == wBo:
                                protected[y, i] += protectionMultiplier(boardIn[y, i])
                                protecting[y, x] += protectionMultiplier(boardIn[y, i])
                                break
                            else:
                                moveList.append(Move(x, y, i, y, wBo))

                case "n" | "N":
                    xs = []
                    ys = []
                    if x > 1 and y < 7:  # 2 left, 1 down
                        xs.append(x - 2)
                        ys.append(y + 1)
                    if x > 1 and y > 0:  # 2 left, 1 up
                        xs.append(x - 2)
                        ys.append(y - 1)
                    if x > 0 and y < 6:  # 1 left, 2 down
                        xs.append(x - 1)
                        ys.append(y + 2)
                    if x > 0 and y > 1:  # 1 left, 2 up
                        xs.append(x - 1)
                        ys.append(y - 2)
                    if x < 6 and y < 7:  # 2 right, 1 down
                        xs.append(x + 2)
                        ys.append(y + 1)
                    if x < 6 and y > 0:  # 2 right, 1 up
                        xs.append(x + 2)
                        ys.append(y - 1)
                    if x < 7 and y < 6:  # 1 right, 2 down
                        xs.append(x + 1)
                        ys.append(y + 2)
                    if x < 7 and y > 1:  # 1 right, 2 up
                        xs.append(x + 1)
                        ys.append(y - 2)
                    for i in range(len(xs)):
                        wBn = whiteBlack(boardIn[ys[i], xs[i]])
                        if wBn == -1 * wBo:
                            moveList.append(Move(x, y, xs[i], ys[i], wBo))
                            attacked[ys[i], xs[i]] += attackMultiplier(boardIn[ys[i], xs[i]])
                            attacking[y, x] += attackMultiplier(boardIn[ys[i], xs[i]])
                        elif wBn == wBo:
                            protected[ys[i], xs[i]] += protectionMultiplier(boardIn[ys[i], xs[i]])
                            protecting[y, x] += protectionMultiplier(boardIn[ys[i], xs[i]])
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
                                attacking[y, x] += attackMultiplier(boardIn[y + 1, x - 1])
                            elif wBn == wBo:
                                protected[y + 1, x - 1] += protectionMultiplier(boardIn[y + 1, x - 1])
                                protecting[y, x] += protectionMultiplier(boardIn[y + 1, x - 1])
                        if x < 7:
                            wBn = whiteBlack(boardIn[y + 1, x + 1])
                            if wBn == -1 * wBo:
                                moveList.append(Move(x, y, x + 1, y + 1, wBo))
                                attacked[y + 1, x + 1] += attackMultiplier(boardIn[y + 1, x + 1])
                                attacking[y, x] += attackMultiplier(boardIn[y + 1, x + 1])
                            elif wBn == wBo:
                                protected[y + 1, x + 1] += protectionMultiplier(boardIn[y + 1, x + 1])
                                protecting[y, x] += protectionMultiplier(boardIn[y + 1, x + 1])

                    if y == 1:
                        if whiteBlack(boardIn[y + 1, x]) == 0 and whiteBlack(boardIn[y + 2, x]) == 0:
                            moveList.append(Move(x, y, x, y + 2, wBo))

                case "P":
                    if y > 0:
                        if whiteBlack(boardIn[y - 1, x]) == 0:
                            moveList.append(Move(x, y, x, y - 1, wBo))
                        if x > 0:
                            wB = whiteBlack(boardIn[y - 1, x - 1])
                            if wB == -1 * wBo:
                                moveList.append(Move(x, y, x - 1, y - 1, wBo))
                                attacked[y - 1, x - 1] += attackMultiplier(boardIn[y - 1, x - 1])
                                attacking[y, x] += attackMultiplier(boardIn[y - 1, x - 1])
                            elif wB == wBo:
                                protected[y - 1, x - 1] += protectionMultiplier(boardIn[y - 1, x - 1])
                                protecting[y, x] += protectionMultiplier(boardIn[y - 1, x - 1])
                        if x < 7:
                            wB = whiteBlack(boardIn[y - 1, x + 1])
                            if wB == -1 * wBo:
                                moveList.append(Move(x, y, x + 1, y - 1, wBo))
                                attacked[y - 1, x + 1] += attackMultiplier(boardIn[y - 1, x + 1])
                                attacking[y, x] += attackMultiplier(boardIn[y - 1, x + 1])
                            elif wB == wBo:
                                protected[y - 1, x + 1] += protectionMultiplier(boardIn[y - 1, x + 1])
                                protecting[y, x] += protectionMultiplier(boardIn[y - 1, x + 1])
                    if y == 6:
                        if whiteBlack(boardIn[y - 1, x]) == 0 and whiteBlack(boardIn[y - 2, x]) == 0:
                            moveList.append(Move(x, y, x, y - 2, wBo))


    return moveList, [attacked, attacking, protected, protecting]


def scoreAnalyzer(boardIn, APIn, moveListIn):
    pawnProgressionModifier = 0.05
    score = 0
    whiteChecked = False
    blackChecked = False
    for y in range(8):
        for x in range(8):
            APCheck = checkAP(APIn, x, y)
            checkSquare = boardIn[y, x]
            score += (whiteBlack(checkSquare) * APModifierLogic(APCheck) + whiteBlack(checkSquare) * valueMultiplier(checkSquare))
            match checkSquare:
                case "k":
                    if APCheck[0] != 0:
                        blackChecked = True
                case "p":
                    score -= 1 * (pawnProgressionModifier*y)
                case "K":
                    if APCheck[0] != 0:
                        whiteChecked = True
                case "P":
                    score += 1 * (pawnProgressionModifier*(7-y))
    # print(whiteChecked, blackChecked)
    return score, whiteChecked, blackChecked


def checkAP(APin, x, y):
    ated = APin[0]
    atin = APin[1]
    pred = APin[2]
    prin = APin[3]
    return [ated[y, x], atin[y, x], pred[y, x], prin[y, x]]


def APModifierLogic(APin):  # 0-Attacked, 1-Attacking, 2-Protected, 3-Protecting
    score = 0
    # score += (APin[2] + APin[3] + APin[1] - APin[0])
    attacked = APin[0]
    attacking = APin[1]
    protected = APin[2]
    protecting = APin[3]

    isolationAttackModifier = 2
    isolationDefendModifier = 0.5

    if attacking != 0 and attacked != 0 and protected != 0:
        score += protected + protecting + attacking - attacked
    elif attacking != 0 and attacked == 0:
        score += protected + protecting + attacking*isolationAttackModifier
    elif attacking != 0 and attacked != 0 and protected == 0:
        score -= attacking + attacked - protecting
    elif attacking != 0:
        score += attacked + protected + protecting

    if attacked != 0 and protected == 0:
        score -= attacked*isolationAttackModifier
    if protected != 0 and attacked == 0 and attacking == 0:
        score += (protected + protecting)*isolationDefendModifier

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
            multiplier = 1
        case "n":
            multiplier = 1
        case "b":
            multiplier = 1
        case "q":
            multiplier = 0.5
        case "k":
            multiplier = 0.1
        case "p":
            multiplier = 0.1
    return multiplier


def attackMultiplier(x):
    multiplier = 0
    match x.lower():
        case "r":
            multiplier = 2
        case "n":
            multiplier = 1.5
        case "b":
            multiplier = 1.5
        case "q":
            multiplier = 5
        case "k":
            multiplier = 5
        case "p":
            multiplier = 0.1
    return multiplier


def valueMultiplier(x):
    value = 0
    match x.lower():
        case "r":
            value = 9
        case "n":
            value = 6
        case "b":
            value = 6
        case "q":
            value = 15
        case "k":
            value = 15
        case "p":
            value = 1
    return value


def convertCoordsToNotation(xo, yo, xn, yn):
    notation = str(chr(xo + 97)) + str((8 - yo)) + str(chr(xn + 97)) + str((8 - yn))
    return notation


def convertNotationToCoords(notation):
    temp = []
    for i in notation:
        temp.append(i)
    xo = ord(temp[0]) - 97
    yo = 8 - int(temp[1])
    xn = ord(temp[2]) - 97
    yn = 8 - int(temp[3])

    return [xo, yo, xn, yn]


def alterBoardForMove(moveIn: Move, boardIn):
    boardOut = boardIn.copy()
    boardOut[moveIn.yn, moveIn.xn] = boardOut[moveIn.yo, moveIn.xo]
    boardOut[moveIn.yo, moveIn.xo] = "."
    return boardOut


def getBestMove(board, wB, printEnable, depth):
    moveList, APArray = moveAnalyzer(board)

    if printEnable:
        moveListW = []
        moveListB = []
        for i in moveList:
            if i.wB == 1:
                moveListW.append(i.__str__())
            else:
                moveListB.append(i.__str__())

        print("\nWhite moves:")
        print(moveListW)
        print("\nBlack moves:")
        print(moveListB)

    currScore, whiteChecked, blackChecked = scoreAnalyzer(board, APArray, moveList)

    if printEnable:
        print("\nCurrent analysis: ", round(currScore, 3))
        print("Check status [White]:", whiteChecked)
        print("Check status [Black]:", blackChecked)

    bestMove = ""
    bestScore = -1000*wB

    for moveCheck in moveList:
        if moveCheck.wB == wB:

            newBoard = alterBoardForMove(moveCheck, board)
            newMovelist, newAP = moveAnalyzer(newBoard)
            newScore, newWC, newBC = scoreAnalyzer(newBoard, newAP, newMovelist)

            if printEnable:
                #print(wB, newWC, newBC)
                if wB == WHITE:
                    print(moveCheck, np.round(newScore, 3))
                else:
                    print(moveCheck, np.round(newScore, 3))
                # print("Old board:", board)
                # print("New board:", newBoard)

            if whiteChecked and wB == WHITE:
                if not newWC:
                    if newScore > bestScore and wB == WHITE:
                        bestScore = newScore
                        bestMove = moveCheck
                    elif newScore < bestScore and wB == BLACK:
                        bestScore = newScore
                        bestMove = moveCheck

            elif blackChecked and wB == BLACK:
                if not newBC:
                    if newScore > bestScore and wB == WHITE:
                        bestScore = newScore
                        bestMove = moveCheck
                    elif newScore < bestScore and wB == BLACK:
                        bestScore = newScore
                        bestMove = moveCheck
            else:
                if newScore > bestScore and wB == WHITE:
                    bestScore = newScore
                    bestMove = moveCheck
                elif newScore < bestScore and wB == BLACK:
                    bestScore = newScore
                    bestMove = moveCheck

    if printEnable:
        if (bestScore == -1000 and wB == WHITE) or (bestScore == 1000 and wB == BLACK):
            print("You have no available moves, and have lost the game!")
        else:
            print("\nYour best is: ")
            print(bestMove)
            print(" with a score of ")
            print(bestScore)

    return bestMove
