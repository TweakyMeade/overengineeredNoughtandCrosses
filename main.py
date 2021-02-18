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
    return 'x'
def winQuestion(fR, sR, tR):
    if fR[0] == sR[0] == tR[0]:
        return True
    if fR[1] == sR[1] == tR[1]:
        return True
    if fR[2] == sR[2] == tR[2]:
        return True


printBoard(rOne, rTwo, rThree)
playerCounter = 1

while True:



