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

gameData = input()
if gameData == "isready":
    gameData = input()

gameData.split(" ")
if(gameData[1] == "startpos"):
