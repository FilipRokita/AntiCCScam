import random



def randomcc():
    cc = ''
    temp = ''
    for i in range(4):
        for i in range(4):
            temp = temp + str(random.randint(0, 9))
        cc = cc + temp + ' '
        temp = ''
    return cc[:-1]


def randomexp():
    exp = ''
    temp = ''
    exp = exp + str(random.randint(0, 1))
    exp = exp + str(random.randint(0, 2))
    exp = exp + '/'
    exp = exp + str(random.randint(0, 2))
    exp = exp + str(random.randint(1, 9))
    return exp


def randomcvv():
    cvv = ''
    temp = ''
    for i in range(3):
        temp = str(random.randint(0,9))
        cvv = cvv + temp
    return cvv