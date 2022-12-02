import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
print(lines)


def calc(letter):
    if letter == 'X':
        return 1
    elif letter == 'Y':
        return 2
    elif letter == 'Z':
        return 3
    else:
        raise "Not a valid letter!"


def calc_game(opponent, my):
    if opponent == 'A' and my == 'Y' or opponent == 'B' and my == 'Z' or opponent == 'C' and my == 'X':
        return 6 + calc(my)
    elif opponent == 'A' and my == 'Z' or opponent == 'B' and my == 'X' or opponent == 'C' and my == 'Y':
        return 0 + calc(my)
    else:
        return 3 + calc(my)


win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}
draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

res1 = 0
res2 = 0
for a in lines:
    opponent_letter, my_letter = a.split(' ')

    res1 += calc_game(opponent_letter, my_letter)

    if my_letter == 'X':
        my_letter = lose[opponent_letter]
    elif my_letter == 'Y':
        my_letter = draw[opponent_letter]
    elif my_letter == 'Z':
        my_letter = win[opponent_letter]

    res2 += calc_game(opponent_letter, my_letter)

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {res2}')
