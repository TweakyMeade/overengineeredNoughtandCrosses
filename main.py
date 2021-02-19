rOne = ['-','-','-']
rTwo = ['-','-','-']
rThree = ['-','-','-']
def printBoard(fR, sR, tR):
    print(fR)
    print(sR)
    print(tR)
    print('\n')
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
def playerAction(row,column,pCount):
    row[column] = returnCounter(pCount)

def inputFunc(pCount,rowOne, rowTwo, rowThree):
    x = int(input('Which row do you choose? "1","2" or "3":'))
    y = int(input('Which column do you choose? "1","2" or "3"')) - 1
    if int(x) == 1:
        if prodAns(rowOne, int(y),):
            playerAction(rowOne, int(y), pCount)
            return True
    if int(x) == 2:
        if prodAns(rowTwo, int(y),):
            playerAction(rowTwo, int(y), pCount)
            return True
    if int(x) == 3:
        if prodAns(rowThree, int(y),):
            playerAction(rowThree, int(y), pCount)
            return True
    return False
def whoIsPlaying(pCount):
    if pCount % 2 == 0:
        print('Now its 0!')
    else:
        print('now its X go!')
def prodAns(row,column):
    return row[column] == '-'



print("Welcome to 0's and X's!")
startFlag = True
while startFlag:
    chooser = input('what do you want start with "X" or "O":').upper()
    if chooser == "X":
        playerCount = 1
        startFlag = False
    elif chooser == "0" or "O":
        playerCount = 2
        startFlag = False
    else:
        print("You've not made a vaild selection")
flag = True
while flag:
    printBoard(rOne,rTwo,rThree)
    whoIsPlaying(playerCount)
    restarter = inputFunc(playerCount, rOne, rTwo, rThree)
    if restarter:
        playerCount += 1
    else:
        print('that was an invalid input try again')
    if winQuestion(rOne, rTwo, rThree):
        print("YOU ARE WINNER:", returnCounter(playerCount-1))
        flag = False
print("an over thought out solution, to an easy program")
