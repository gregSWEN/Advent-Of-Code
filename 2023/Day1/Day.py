

def main():
    with open("input.txt") as file:
        lines = file.readlines()
        word_numbers = {"one": 1, "two": 2, "three": 3, "four": 4,
                        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        sum = 0
        for line in lines:
            line = line.strip()
            num = []
            index = len(line) + 1
            numberFound = None
            index_first_num = get_index_first_num(line)

            for key in word_numbers.keys():
                if key in line:
                    if index > line.find(key):
                        index = line.find(key)
                        numberFound = key

            if index_first_num < index:
                num.append(int(line[index_first_num]))
            else:
                num.append(word_numbers[numberFound])
            index_last_num = get_index_last_num(line)
            index = -100
            for key in word_numbers.keys():
                if key in line:
                    if index < line.rfind(key):
                        index = line.rfind(key)
                        numberFound = key
            if index_last_num > index:
                num.append(int(line[index_last_num]))
            else:
                num.append(word_numbers[numberFound])

            sum += (num[0] * 10) + num[1]
            print(num)
        print(sum)


def get_index_first_num(line):
    for i in range(0, len(line)):
        if line[i].isnumeric():
            return i
    return 10000


def get_index_last_num(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            return i
    return -100


if __name__ == "__main__":
    main()
