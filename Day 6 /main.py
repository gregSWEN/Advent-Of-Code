from re import L


filename = 'data.txt'

# Add the 4 numbers into a Set,
# Whle the set is still less than 4 in length, increment
# winstart and win end, and remove the
# character that appears at winStart and
# add the character that appears at win end


def main():
    with open(filename) as file:
        lines = file.readlines()
        word = lines[0]
        win_start = 0
        win_end = 13
        mySet = {}
        for i in range(win_end + 1):
            letter = word[i]
            if letter not in mySet:
                mySet[letter] = 1
            else:
                mySet[letter] += 1

        while (len(mySet) < 14):
            win_end += 1
            new_letter = word[win_end]
            old_letter = word[win_start]
            if new_letter not in mySet:
                mySet[new_letter] = 1
            else:
                mySet[new_letter] += 1
            # print(mySet, old_letter)
            mySet[old_letter] -= 1  # remove(word[win_start])
            if mySet[old_letter] == 0:
                del mySet[old_letter]
            win_start += 1

    print(win_end + 1)


main()
