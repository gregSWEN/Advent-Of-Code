INDEX_OF_OPPONENT = 0
INDEX_OF_MYSELF = 2

map = {'X': 1, 'Y': 2, 'Z': 3}


# ROCK, PAPER SCISSORS
xyz_map = {'X': 0, 'Y': 1, 'Z': 2}
abc_map = {'A': 0, 'B': 1, 'C': 2}
win_lose_matrix = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]


def get_points_win_loss(opponent, myself):
    result = win_lose_matrix[xyz_map[myself]][abc_map[opponent]]
    if result == -1:
        return 0
    elif result == 0:
        return 3
    elif result == 1:
        return 6


def get_points(opponent, myself):
    points = 0
    points += map[myself]
    points += get_points_win_loss(opponent, myself)
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
