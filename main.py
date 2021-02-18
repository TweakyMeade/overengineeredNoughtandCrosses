rOne = ['-','-','-']
rTwo = ['-','-','-']
rThree = ['-','=','-']
def printBoard(fR, sR, tR):
    print(fR)
    print(sR)
    print(tR)
    print('\n')
def returnCounter(count):
    if count % 2 == 0:
        return '0'
    return 'x'
def winQuestion(fR, sR, tR):
    if fR[0] == sR[0] == tR[0]:
        return True
    if fR[1] == sR[1] == tR[1]:
        return True
    if fR[2] == sR[2] == tR[2]:
        return True
    if fR[0] == sR[1] == tR[2]:
        return True
    if fR[2] == sR[1] == tR[0]:
        return True
    if fR[0] == fR[1] == fR[2]:
        return True
    if sR[0] == sR[1] == sR[2]:
        return True
    if tR[0] == tR[1] == tR[2]:
        return True
    return False

printBoard(rOne, rTwo, rThree)
a = winQuestion(rOne,rTwo,rThree)
print(a)


