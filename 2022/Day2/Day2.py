"""
A simple game of rock paper scissors amongst Elves
You are given a sheet of outcomes (two columns)
The 1st value is what will be played by your opponent
The 2nd value is : { pt1: what you should play against your opponent (rock/paper/scissors)
                   { pt2: your suggested action (win/lose/draw)
Given that you get 1,2,3 pts for playing r/p/s
And you get 0,3,6 for lose/draw/win

What are your total points in each part?
"""


col1_guide = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
pt1_guide = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
pt1_guide_add = {
    'X': {'A': 'draw', 'B': 'lose', 'C': 'win'},
    'Y': {'A': 'win', 'B': 'draw', 'C': 'lose'},
    'Z': {'A': 'lose', 'B': 'win', 'C': 'draw'}
}
pt2_guide = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
pt2_guide_add = {
    'lose': {'A': 'Z', 'B': 'X', 'C': 'Y'},
    'draw': {'A': 'X', 'B': 'Y', 'C': 'Z'},
    'win': {'A': 'Y', 'B': 'Z', 'C': 'X'}
}

pt1_score = {'rock': 1, 'paper': 2, 'scissors': 3}
pt2_score = {'lose': 0, 'draw': 3, 'win': 6}


def play_outcome(in_val: str) -> int:
    return pt1_score[pt1_guide[in_val]]


def pt1_score_outcome(in1: str, in2: str) -> int:
    # Read in tuple of inputs
    # in2 tells us what we play, in1 tells us what our opponent plays
    return pt2_score[pt1_guide_add[in2][in1]] + play_outcome(in2)


def pt2_score_outcome(in1: str, in2: str) -> int:
    # Read in a tuple of inputs
    # in2 tells us action (win/lose/draw), in1 tells us outcome (what we play)
    action = pt2_guide[in2]
    return pt2_score[action] + play_outcome(pt2_guide_add[action][in1])


with open('input.txt') as f:
    play_sum_rd1 = 0
    play_sum_rd2 = 0
    for line in f.readlines():
        line_vals = line.rstrip().split(' ')
        play_sum_rd1 += pt1_score_outcome(line_vals[0], line_vals[1])
        play_sum_rd2 += pt2_score_outcome(line_vals[0], line_vals[1])

print(play_sum_rd1)
print(play_sum_rd2)

"""
11150
8295
"""