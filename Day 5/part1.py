import re

arr = [['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M'],
       ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H'],
       ['W', 'R', 'C', 'D', 'G'],
       ['N', 'B', 'S'],
       ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N'],
       ['P', 'R', 'M', 'W'],
       ['R', 'T', 'N', 'G', 'L', 'S', 'W'],
       ['Q', 'T', 'H', 'F', 'N', 'B', 'V'],
       ['L', 'M', 'H', 'Z', 'N', 'F']]

# arr = [['Z', 'N'],
#        ['M', 'C', 'D'],
#        ['P']
#        ]

# ITS NOT - WJSSNWWVF


def conduct_move(amount, from_dest, to_dest):
    new_arr = []
    for i in range(amount):
        # Make an array
        new_arr.append(arr[from_dest].pop())

    for i in range(amount):
        arr[to_dest].append(new_arr.pop())


def main():
    with open('data.txt') as file:
        lines = file.readlines()
        for move in lines:
            map_of_nums = map(int, re.findall('\d+', move))
            list_of_nums = (list(map_of_nums))
            conduct_move(list_of_nums[0],
                         list_of_nums[1]-1,  list_of_nums[2]-1)

    for i in range(len(arr)):
        print(arr[i].pop(), end="")


main()
