def calc_total(arr):
    sum = 0
    for x in arr:
        sum += int(x.strip('\n'))
    return sum


def main():
    with open('data.txt') as file:
        lines = file.readlines()
        max_sum, curr_sum = 0, 0

        curr_arr, to_sort_array = [], []
        for line in lines:
            if line == '\n':
                to_sort_array.append(calc_total(curr_arr))
                max_sum = max(calc_total(curr_arr), max_sum)
                curr_arr = []
            else:
                curr_arr.append(line)
        to_sort_array.sort(reverse=True)
        print(to_sort_array[0] + to_sort_array[1] + to_sort_array[2])


main()
