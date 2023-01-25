# 한 문자열이 주어졌을 때, 잘 수 있는지 확인
def isOktoSleep(oneLine):
    marginList = oneLine.split('X')
    for list in marginList:
        if (len(list) > 1):
            return True
    return False


# 해당 열에 위치한 문자열 추출
def getColumn(x, room):
    column = []
    for line in room:
        column.append(line[x])
    return column


number = int(input())
room = [list(input()) for _ in range(number)]
print(room)

row = [''.join(line) for line in room]
column = [''.join(getColumn(i, room)) for i in range(number)]

rowCount, columnCount = 0, 0

for i in range(number):
    if isOktoSleep(row[i]): rowCount += 1
    if isOktoSleep(column[i]): columnCount += 1

print(rowCount, columnCount)