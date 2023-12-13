

def count_winning_scorecards(line):

    _, number_string = line.split(":")

    winning_nums, guessed_nums = [num.split()
                                  for num in number_string.strip().split("|")]
    count = sum(1 for num in guessed_nums if num in winning_nums)

    if count == 0:
        return 0
    else:
        return 2 ** (count - 1)


with open("input.txt") as file:
    lines = []
    for line in file:
        lines.append(line.strip())

sum_count = 0
for line in lines:
    sum_count += count_winning_scorecards(line)

print(sum_count)
