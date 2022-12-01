"""
Player 1 starting position: 8
Player 2 starting position: 3
3 4 5 6 7 8 9
1           1
1
1   1
1   2   1
1   3   3   1
1   4   6   4   1
1   5   10  10  5   1
1   6   15  20  15  6   1
1367631

3: [111]
4: [112], [121], [211]
5: [113], [122], [131], [212], [221], [311]
6: [123], [132], [213], [222], [231], [312], [321]
7: [133], [223], [232], [313], [322], [331]
8: [233], [323], [332]
9: [333]

"""
import numpy as np


class player:
    def __init__(self, name, start_position):
        self.name = name
        self.position = start_position
        self.score = 0

    def die_roll(self, die_value):
        temp_position = self.position + die_value
        if temp_position % 10 == 0:
            self.position = 10
        else:
            self.position = temp_position % 10

def roll_three_times(roll_counter):
    new_roll_set, new_sum_roll = 3, 0
    while new_roll_set > 0:
        roll_counter += 1
        if roll_counter % 100 == 0:
            sum_die = 100
        else:
            sum_die = roll_counter % 100
        new_sum_roll += sum_die
        new_roll_set -= 1
    return roll_counter, new_sum_roll


def player_outcome(player_start_position):
    player_position_universe = []
    player_positions_over_21 = []
    possible_outcomes = [i for i in range(3, 10)]
    outcome_multiplier_dictionary = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    for moves in possible_outcomes:
        moves_multiplier = outcome_multiplier_dictionary[moves]
        player_position_universe.append([moves_multiplier, [position_update(player_start_position, moves)]])
    while len(player_position_universe) > 0:
        potential_outcome = player_position_universe.pop(0)
        for moves in possible_outcomes:
            temp_multiplier = potential_outcome[0] * moves
            temp_outcome = potential_outcome[1].copy()
            temp_outcome.append(position_update(temp_outcome[-1], moves))
            if np.sum(temp_outcome) > 21:
                player_positions_over_21.append([temp_multiplier, temp_outcome])
            else:
                player_position_universe.append([temp_multiplier, temp_outcome])
    return player_positions_over_21

def player_dictionary_outcomes(universe_list):
    min_val = min([len(sublist[1]) for sublist in universe_list])
    max_val = max([len(sublist[1]) for sublist in universe_list])
    player_dictionary = {i: 0 for i in range(min_val, max_val)}
    for key in player_dictionary.keys():
        player_dictionary[key] = sum([sublist[0] for sublist in universe_list if len(sublist[1]) == key])
    return player_dictionary


def compare_dictionary(dict1: dict, dict2:dict):
    total_wins_1, total_wins_2, total_ties = 0, 0, 0
    for key1 in dict1.keys():
        for key2 in dict2.keys():
            matches_won = dict1[key1] * dict2[key2]
            if key1 < key2:
                total_wins_1 += matches_won
            elif key1 > key2:
                total_wins_2 += matches_won
            else:
                total_ties += matches_won
    print(f"the left dict won: {total_wins_1}, where the right won: {total_wins_2} and total ties: {total_ties}")

# play game, update scores and number of occurances each occur
# have a multiplier, have a score
# each rd of game:
# player1 updates positions, has possible outcomes
# player2 updates positions, updates those possible outcomes


total_wins_1, total_wins_2 = 0, 0
for key in player1_dict_outcomes.keys():
    multiplier = player1_dict_outcomes[key]
    for key2 in player2_dict_outcomes.keys():
        wins = player1_dict_outcomes[key] * player2_dict_outcomes[key2]
        if key <= key2:
            total_wins_1 += wins
        else:   ##key2 < key1
            total_wins_2 += wins
print(f"player1 wins in {player1_wins} universes.")
print(f"player2 wins in {player2_wins} universes.")


def position_update(initial_position, advancement):
    temp_position = initial_position + advancement
    if temp_position % 10 == 0:
        return 10
    else:
        return temp_position % 10

# create a list of moves for each player (universe of possible outcomes
# for each new rollset in that list, append
# start at 8, possible outcomes = [3,4,5,6,7,8,9]
# so first roll generates: [1, 2, 3, 4, 5, 6, 7]
# second roll, for each first roll:
# [ [1, 4], [1,5], [1,6], [1,7], [1,8], [1,9], [1,10], [2, 5], [2, 6] ...]
# once a run has hit 21, pop it and add to list of over_21
# compare player universes to see all possible outcomes
# play_game
#   take game state
#   play p1
#   check win
#   play p2
#   check win
# list of all game states & multiples of game states


player1_position, player2_position = 8, 4
player1_score, player2_score = 0, 0
game_state = {'p1_position': player1_position, 'p1_score': player1_score, 'p2_position': player2_position, 'p2_score': player2_score}
possible_outcomes = [i for i in range(3, 10)]
outcome_multiplier_dictionary = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
list_of_game_states = [[1, game_state]]
player1_wins, player2_wins = 0, 0
while len(list_of_game_states) > 0:
    new_game_state = list_of_game_states.pop()
    multiple = new_game_state[0]
    game_state = new_game_state[1]
    for moves in possible_outcomes:
        multiplier = multiple * outcome_multiplier_dictionary[moves]
        additional_game_state = game_state.copy()
        additional_game_state['p1_position'] = position_update(additional_game_state['p1_position'], moves)
        additional_game_state['p1_score'] += additional_game_state['p1_position']
        if additional_game_state['p1_score'] > 20:
            player1_wins += multiplier
        else:
            for move2 in possible_outcomes:
                new_multiplier = multiplier * outcome_multiplier_dictionary[move2]
                addt_game_state = additional_game_state.copy()
                addt_game_state['p2_position'] = position_update(addt_game_state['p2_position'], move2)
                addt_game_state['p2_score'] += addt_game_state['p2_position']
                if addt_game_state['p2_score'] > 20:
                    player2_wins += multiplier
                else:
                    list_of_game_states.append([new_multiplier, addt_game_state])
    del new_game_state
print(f"there are {len(list_of_game_states)} remaining. current_score: {player1_wins}-{player2_wins}.")



    # roll die 3 times
    # roll counter can act as roll with %100
    # sum up to get move
    # (player_position + sum)%10 is new space
    # add space to player score
