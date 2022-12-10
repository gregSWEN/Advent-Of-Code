filename = 'data.txt'


def calc_priority(letter):
    if ord(letter) > 95:  # Lowercase
        priority = ord(letter) - 96
    else:
        priority = ord(letter) - 38

    return priority


def sum_arr(arr):
    sum = 0
    for elt in arr:
        sum += elt
    return sum


# Read one line at a time add that line to the set,
#

with open(filename) as file:
    lines = file.readlines()
    main_array = []
    map = set()
    map2 = set()
    map3 = set()
    for rucksack in lines:
        if len(map) == 0:
            for i in range(len(rucksack)):
                map.add(rucksack[i])

        elif len(map2) == 0:
            for j in range(len(rucksack)):
                map2.add(rucksack[j])
        elif len(map3) == 0:
            for k in range(len(rucksack)):
                map3.add(rucksack[k])
            for elt in map2:
                if elt in map and elt in map3 and elt != '\n':
                    main_array.append(calc_priority(elt))
            map = set()
            map2 = set()
            map3 = set()

    print(sum_arr(main_array))
