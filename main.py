
def XOChoice():
    while True:
        chooser = input('What do you want start with "X" or "O"?:').upper()
        if chooser == "X":
            return int(1)

        if chooser == "O":
            return int(2)
        print("You've not made a valid selection!")
def printBoard(fR, sR, tR):
    print('')
    fRS = fR[0] + fR[1] + fR[2]
    sRS = sR[0] + sR[1] + sR[2]
    tRS = tR[0] + tR[1] + tR[2]
    print('% 123')
    print('1', fRS)
    print('2', sRS)
    print('3', tRS)
def returnCounter(count):
    if count % 2 == 0:
        return '0'
    return 'X'
def winQuestion(fR, sR, tR):
    if fR[0] == sR[0] == tR[0] != '-':
        return True
    if fR[1] == sR[1] == tR[1] != '-':
        return True
    if fR[2] == sR[2] == tR[2] != '-':
        return True
    if fR[0] == sR[1] == tR[2] != '-':
        return True
    if fR[2] == sR[1] == tR[0] != '-':
        return True
    if fR[0] == fR[1] == fR[2] != '-':
        return True
    if sR[0] == sR[1] == sR[2] != '-':
        return True
    if tR[0] == tR[1] == tR[2] != '-':
        return True
    return False
def playerAction(row, column, pCount):
    row[column] = returnCounter(pCount)
def inputFunc(pCount, rowOne, rowTwo, rowThree):
    x = int(input('Which row do you choose? "1","2" or "3"?:'))
    y = int(input('Which column do you choose? "1","2" or "3"?:')) - 1
    if int(x) == 1:
        if prodAns(rowOne, int(y), ):
            playerAction(rowOne, int(y), pCount)
            return True
    if int(x) == 2:
        if prodAns(rowTwo, int(y), ):
            playerAction(rowTwo, int(y), pCount)
            return True
    if int(x) == 3:
        if prodAns(rowThree, int(y), ):
            playerAction(rowThree, int(y), pCount)
            return True
    return False
def whoIsPlaying(pCount):
    if pCount % 2 == 0:
        print("Now it's 0 go!!")
    else:
        print("now it's X go!")
def prodAns(row, column):
    return row[column] == '-'
print("Welcome to 0's and X's!")
rOne = ['-', '-', '-']
rTwo = ['-', '-', '-']
rThree = ['-', '-', '-']
playerCount = XOChoice()
roundCount = 9
while True:
    printBoard(rOne, rTwo, rThree)
    whoIsPlaying(playerCount)
    gRestart = inputFunc(playerCount, rOne, rTwo, rThree)
    if gRestart:
        playerCount += 1
        roundCount -= 1
    else:
        print('That was an invalid input, try again!')
    if winQuestion(rOne, rTwo, rThree):
        printBoard(rOne, rTwo, rThree)
        print("YOU ARE THE WINNER:", returnCounter(playerCount - 1))
        break
    if roundCount == 0:
        print("NO ONE WINS THE EASIEST GAME IN THE WORLD!")
        break
print("\nAn over thought out solution, to an easy program!")
