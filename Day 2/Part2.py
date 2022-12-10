
INDEX_OF_OPPONENT = 0
INDEX_OF_MYSELF = 2

# X = lose, Y = Tie, Z = Win

# ROCK, PAPER SCISSORS


win_loss_map = {'X': 0, 'Y': 3, 'Z': 6}

abc_map = {'A': 0, 'B': 1, 'C': 2}
xyz_map = {'X': 0, 'Y': 1, 'Z': 2}

#                     lose,      draw        win
win_lose_matrix = [[2, 0, 1], [0, 1, 2], [1, 2, 0]]


# if x in xyz_map.values()

def get_points_win_loss(opponent, myself):
    result = win_lose_matrix[xyz_map[myself]][abc_map[opponent]]
    if result == 0:  # Rock
        return 1
    elif result == 1:  # Paper
        return 2
    elif result == 2:  # Scissors
        return 3


def get_points(opponent, myself):
    points = 0
    points += win_loss_map[myself]  # 3, 0, 6,
    points += get_points_win_loss(opponent, myself)  # 1, 1,

    return points


def main():
    with open('data.txt') as file:
        total_score = 0
        lines = file.readlines()
        for match in lines:
            total_score += get_points(match[INDEX_OF_OPPONENT],
                                      match[INDEX_OF_MYSELF])

    print(total_score)


main()
