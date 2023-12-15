from cmath import inf


def calculate_soil(lines, seed):
    line_num = 0  # Line
    new_segment = False
    while line_num < len(lines):
        curr_line = lines[line_num].split(" ")
        if "map:" not in curr_line:
            print(curr_line)
            # Compute calculation
            difference = int(curr_line[1]) - int(curr_line[0])
            print("finished difference calculation")
            start = int(curr_line[1])
            end = int(curr_line[1]) + int(curr_line[2])
            if seed >= start and seed < end and new_segment:
                # for num in range(int(curr_line[1]), int(curr_line[1]) + int(curr_line[2])):
                #     print("Checking if statement")
                #     if seed == num and new_segment:
                seed -= difference
                new_segment = False
        else:
            new_segment = True
        line_num += 1
    return seed


with open("input.txt") as file:
    lines = []
    seeds = file.readline().strip().split(":")[1].strip().split(" ")
    seeds = [int(seed) for seed in seeds]
    lines = [line.strip() for line in file.readlines() if line.strip() != '']
    minimum = inf

    print(min(calculate_soil(lines, seed) for seed in seeds))


# Check Each line and see if that seed is in the range. If it is, calculate it.
