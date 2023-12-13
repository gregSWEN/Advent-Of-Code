from collections import deque


def count_matches(line):
    parts = line.split(":")
    winning_nums, guessed_nums = parts[1].strip().split("|")
    winning_nums = set(winning_nums.split())
    guessed_nums = guessed_nums.split()

    count = sum(num in winning_nums for num in guessed_nums if num)
    return count


def process_cards(lines):
    card_counts = [0] * len(lines)  # Array to track counts for each card
    to_process = deque(range(len(lines)))  # Queue with indices of the cards

    while to_process:
        card_index = to_process.popleft()
        matches = count_matches(lines[card_index])
        card_counts[card_index] += 1

        # Enqueue the copies of subsequent cards
        for i in range(1, matches + 1):
            next_card_index = card_index + i
            if next_card_index < len(lines):
                to_process.append(next_card_index)

    return sum(card_counts)


with open("input.txt") as file:
    lines = [line.strip() for line in file]

total_cards = process_cards(lines)
print(total_cards)
