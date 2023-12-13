

def count_winning(line):
    line = line.split(":")
    line = line[1].strip().split("|")

    winning_nums = line[0].split(" ")
    guessed_nums = line[1].split(" ")
    count = -1
    for num in guessed_nums:
        if num in winning_nums and num != '':
            print(num)
            count += 1

    if count == -1:
        return 0
    else:

        return 2 ** count


with open("input.txt") as file:
    lines = []
    for line in file:
        lines.append(line.strip())

sum = 0
for line in lines:
    sum += count_winning(line)

print(sum)
