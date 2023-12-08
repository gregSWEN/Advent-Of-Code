from curses.ascii import isdigit
symbols = {"*", "$", "#", "+", "/", "=", "&", "(", ")", "@", "%", "-"}


def is_symbol(elt):
    return elt in symbols


def has_adjacent_symbol(i, j, max_i, max_j, arr):
    # (i-1, j-1,), Top left DONE
    # (i-1, j), Right above DONE
    # (i-1, j + 1) top Right DONE
    # (i, j + 1) in front DONE
    # (i + 1, j + 1) bottom right DONE
    # (i + 1, j)  underneath DONE
    # (i + 1, j -1) bottom left
    # (i, j - 1) to the left

    try:
        if i < max_i and j < max_j and i > 0 and j > 0 and is_symbol(arr[i-1][j-1]):
            return True
        if i < max_i and j < max_j and i > 0 and j >= 0 and is_symbol(arr[i-1][j]):
            return True
        if i < max_i and j+1 < max_j and i > 0 and j >= 0 and is_symbol(arr[i-1][j+1]):
            return True
        if i < max_i and j+1 < max_j and i >= 0 and j >= 0 and is_symbol(arr[i][j+1]):
            return True
        if i+1 < max_i and j+1 < max_j and i >= 0 and j >= 0 and is_symbol(arr[i+1][j+1]):
            return True
        if i+1 < max_i and j < max_j and i >= 0 and j >= 0 and is_symbol(arr[i+1][j]):
            return True
        if i+1 < max_i and j < max_j and i >= 0 and j > 0 and is_symbol(arr[i+1][j-1]):
            return True
        if i < max_i and j < max_j and i >= 0 and j > 0 and is_symbol(arr[i][j-1]):
            return True
    except IndexError:
        print(f"i: {i}, max i: {max_i}, j: {j}, max_j {max_j}")


def get_curr_num(i, j, max_j, arr):
    num_arr = []  # Add the first number to the array
    while (True):
        if j < max_j and isdigit(arr[i][j]):
            num_arr.append(arr[i][j])
        else:
            break
        j += 1

    # Sum the numbers
    num_str = ''.join(str(num) for num in num_arr)
    return int(num_str)


def count_gears(arr):
    curr_digit = 0
    gear_sum = 0
    num_added = False
    sum_set = []
    max_i = len(arr)
    max_j = len(arr[0])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (isdigit(arr[i][j])):
                curr_digit += 1
                print(f"Checking {arr[i][j]}")
                if curr_digit == 1:
                    curr_num = get_curr_num(i, j, max_j, arr)
                if curr_digit >= 1 and has_adjacent_symbol(i, j, max_i, max_j, arr) and not num_added:
                    sum_set.append(curr_num)
                    num_added = True
                else:
                    print(f"Checked {arr[i][j]} and didnt find")
            else:
                num_added = False
                curr_digit = 0

    for elt in sum_set:
        print(elt)
        gear_sum += elt
    print(gear_sum)


with open("input.txt") as file:
    lines = []
    for line in file:
        lines.append(line.strip())

    arr = [list(word) for word in lines]
    count_gears(arr)


#  Add all every symbol to a 2-D array
# iterate over the array
# if you come across a digit:
#       figure out if its a part number-
#       go through all possible moves gvein the position  to
#       figure out if its part umber
#
