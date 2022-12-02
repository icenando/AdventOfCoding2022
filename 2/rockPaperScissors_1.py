win = ["AY", "BZ", "CX"]  # 6
loss = ["AZ", "BX", "CY"]  # 3

myPoints = {"Y": 2, "X": 1, "Z": 3}


def partOne(f):
    myTotal = 0
    for playedSymbol in f.readlines():
        result = playedSymbol.replace("\n", "").replace(" ", "")
        if result in win:
            myTotal += 6 + myPoints.get(result[-1])
        elif result in loss:
            myTotal += myPoints.get(result[-1])
        else:
            myTotal += 3 + myPoints.get(result[-1])
    print(myTotal)


def partTwo(f):
    myTotal = 0
    winDict = {"A": "Y", "B": "Z", "C": "X"}
    lossDict = {"A": "Z", "B": "X", "C": "Y"}
    drawDict = {"A": "X", "B": "Y", "C": "Z"}
    for playedSymbol in f.readlines():
        result = playedSymbol.replace("\n", "").replace(" ", "")
        opponentSymbol = result[0]
        mySymbol = result[1]
        if mySymbol == "X":
            myPoints += myPoints.get(lossDict.get(opponentSymbol))
        elif mySymbol == "Y":
            myPoints += 3 + myPoints.get(drawDict.get(opponentSymbol))
        else:
            myPoints += 6 + myPoints.get(winDict.get(opponentSymbol))
    print(myTotal)


with (open("input.txt", "r") as f):
    partOne(f)
    partTwo(f)

# A Y   rock paper
# B X   paper rock
# C Z   scissors scissors

# Rock      1
# Paper     2
# Scissors  3

# Victory   6
# Draw      3
# Loss      0

# X: 1  lose
# Y: 2  draw
# Z: 3  win
