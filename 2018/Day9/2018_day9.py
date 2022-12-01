"""
Elf marbles
"""
from collections import deque, defaultdict

def marbles(players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble%players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


def main(n, score):
    start_list = [0, 1]
    marble_counter, elf_number = 1, 0
    current_index = start_list.index(1)
    marble_score = 0
    participants = elf_list(n)
    while marble_counter < score:
        marble_counter += 1
        elf_number = (elf_number + 1) % n
        insert_index = (current_index + 2)  # want to insert between next and next_next, so next_next = insertindex
        if marble_counter%23 != 0:
            if insert_index > len(start_list):
                insert_index %= len(start_list)
            start_list.insert(insert_index, marble_counter)
        else:
            insert_index -= 9
            marble_score = start_list.pop(insert_index) + marble_counter
            participants[elf_number] += marble_score
        current_index = insert_index
    print(participants, marble_score)
