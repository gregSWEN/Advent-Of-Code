

def isVisibleTop(row, col, arr):
    for i in range(0, row):  # Going down the line till reaching number
        if arr[i][col] >= arr[row][col]:
            return False
    return True


def isVisibleLeft(row, col, arr):
    for i in range(0, col):
        if arr[row][i] >= arr[row][col]:
            return False
    return True


def isVisibleRight(row, col, arr):
    for i in range(len(arr)-1, col, -1):
        if arr[row][i] >= arr[row][col]:
            return False
    return True


def isVisibleBottom(row, col, arr):
    for i in range(len(arr)-1, row, -1):
        if arr[i][col] >= arr[row][col]:
            return False
    return True


with open('data.txt') as file:
    lines = file.readlines()

    mySet = ()
    arr = []
    l = []
    for line in lines:
        line = line.strip('\n')
        row = []
        for number in line:
            row.append(int(number))
        arr.append(row)
    for row in arr:
        print(row, end=',\n')
    totalVisibleCount = 0

    for i in range(1, len(arr)-1):
        for j in range(1, len(arr)-1):
            if isVisibleTop(i, j, arr):
                print(f"{i},{j} is visible from the top")
                l.append([i, j])
            elif isVisibleRight(i, j, arr):
                print(f"{i},{j} is visible from the Right")
                l.append([i, j])
            elif isVisibleBottom(i, j, arr):
                print(f"{i},{j} is visible from the bottom")
                l.append([i, j])
            elif isVisibleLeft(i, j, arr):
                print(f"{i},{j} is visible from the left")
                l.append([i, j])

    mySet = set(tuple(i) for i in l)
    perimTree = (len(arr)*4 + (-4))
    print(len(l) + perimTree)
