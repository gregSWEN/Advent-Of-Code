import re


def main():
    with open("input.txt") as file:
        lines = file.readlines()
        sumLine = 0
        for line in lines:
            line = line.strip().split(":")
            # gameNum = line[0].split(" ")[1]
            redMax = findMax(line[1], "red")
            blueMax = findMax(line[1], "blue")
            greenMax = findMax(line[1], "green")

            sumLine += (redMax*blueMax*greenMax)

            # bags = line[1].split(";")
            # for bag in bags:
            #     isValid = True
            #     print(bag)
            #     dict = {"blue": 0, "red": 0, "green": 0}
            #     dict = count_numbers(dict, bag)
            #     print(dict)
            #     if not is_valid(dict):
            #         isValid = False
            #         break

            # if isValid:
            #     print(f"Game {gameNum}  being added")
            #     sumLine += int(gameNum)

    return sumLine


def findMax(line, color):
    line = line.strip().split(" ")
    maxRed, i = 0, 0
    while i < len(line):
        word = re.sub(r'\W+', '', line[i+1])
        if word == color:
            maxRed = max(int(line[i]), maxRed)
        i += 2

    return maxRed


def is_valid(dict):
    redCount = 0
    blueCount = 0
    greenCount = 0
    for item in dict:
        if item == "red":
            redCount += dict[item]
        if item == "blue":
            blueCount += dict[item]
        if item == "green":
            greenCount += dict[item]

    return redCount <= 12 and greenCount <= 13 and blueCount <= 14


def count_numbers(dict, line):
    line = line.strip().split(" ")
    i = 0
    while i < len(line):
        num = line[i]
        i += 1
        word = line[i]
        word = re.sub(r'\W+', '', word)
        dict[word] += int(num)
        i += 1

    return dict


if __name__ == "__main__":
    print(main())
