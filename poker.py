import random

# initialize poker
def initializeCards():
    total = []
    for i in range(1, 14):
        for j in range(4):
            total.append(i)
    random.shuffle(total)
    return total

# attribute cards
def attributesCards(listT):
    length = int(len(listT)/2)
    p1 = listT[:length]
    p2 = listT[length:]

# game start
def start(p1, p2):
    desktop = []
    while True:
        rounds = 0
        desktop.append(p1[rounds])
        desktop.append(p2[rounds])
        if len(desktop) != len(set(desktop)):
            sameEle = desktop[len(desktop)]
            break
