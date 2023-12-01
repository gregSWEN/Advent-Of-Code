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


with open(filename) as file:
    lines = file.readlines()
    main_array = []
    for rucksack in lines:
        map = set()
        map2 = set()

        first_sack = range(0, int(len(rucksack)/2))
        second_sack = range(int(len(rucksack)/2), len(rucksack))
        for i in first_sack:
            if rucksack[i] != '\n':
                map.add(rucksack[i])
        for j in second_sack:
            if rucksack[j] != '\n':
                map2.add(rucksack[j])

        for elt in map2:
            if elt in map:
                main_array.append(calc_priority(elt))

    print(sum_arr(main_array))
