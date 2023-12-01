import re

filename = 'data.txt'


def determineOverlap(elfOne, elfTwo):

    overlap = False
    if elfOne[0] <= elfTwo[0] and elfTwo[1] <= elfOne[1]:
        overlap = True
    elif elfOne[0] >= elfTwo[0] and elfTwo[1] >= elfOne[1]:
        overlap = True
    return overlap


def main():
    with open(filename) as file:
        lines = file.readlines()
        list_of_nums = []
        for line in lines:
            map_of_nums = map(int, re.findall('\d+', line))
            list_of_nums.append(list(map_of_nums))

    totalOverlaps = 0
    for pair in list_of_nums:
        elfOne = [pair[0], pair[1]]
        elfTwo = [pair[2], pair[3]]
        if (determineOverlap(elfOne, elfTwo)):
            totalOverlaps += 1

    print(totalOverlaps)


main()
