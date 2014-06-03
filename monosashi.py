import sys


def culculate(length, numberofpoint, pointlist):
    existnumberlist = [0 for x in range(length)]
    for i in range(numberofpoint+1):
        for j in range(numberofpoint+1 - i):
            templist = pointlist[i:i+j+1]
            tempsum = 0
            for k in templist:
                tempsum += k
            existnumberlist[tempsum-1] = 1
    if 0 not in existnumberlist:
        print(pointlist)
        #sys.exit()


def makelistofpoint(length, numberofpoint):
    if numberofpoint * (numberofpoint-1)/2 > length:
        print("invalid parameter\n")
        sys.exit()
    pointlist = [0 for x in range(numberofpoint+1)]
    pointlist[0] = 1
    __submakelistofpoint(length, numberofpoint, pointlist, 1, 1)

#再帰的に一コマ分の長さが入ったリストを生成する関数
#numberは次に入れる値、sumは今までの値の合計。sumはlengthを超えないようにする
def __submakelistofpoint(length, numberofpoint, pointlist, flag, sumnum):
    if flag == numberofpoint:
        pointlist[flag] = length - sumnum
        culculate(length, numberofpoint, pointlist)
    else:
        for i in range(length - sumnum + flag - numberofpoint):
            pointlist[flag] = i + 1
            __submakelistofpoint(length, numberofpoint, pointlist, flag+1, sumnum+i+1)


def main():
    argv = sys.argv
    argc = len(argv)
    if argc != 3:
        print("usage: python %s [length_of_monosashi] [number_of_point]") % argv[0]
        sys.exit()
    length = int(argv[1])
    numberofpoint = int(argv[2])
    makelistofpoint(length, numberofpoint)


if __name__ == '__main__':
    main()
