import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

d = {'U': [1, 0],
     'R': [0, 1],
     'L': [0, -1],
     'D': [-1, 0]}

seen = []
H = [0, 0]
T = [0, 0]
seen.append(T)
for line in lines:
    direction = line[0]
    number = int(line.split()[-1])
    for n in range(number):
        H = [x + y for x, y in zip(H, d[direction])]
        if abs(H[0] - T[0]) > 0 and abs(H[1] - T[1]) > 0 and abs(T[0] - H[0]) + abs(T[1] - H[1]) == 3:
            if H[0] > T[0] and H[1] > T[1]:
                T = [T[0] + 1, T[1] + 1]
            elif H[0] > T[0] and H[1] < T[1]:
                T = [T[0] + 1, T[1] - 1]
            elif H[0] < T[0] and H[1] > T[1]:
                T = [T[0] - 1, T[1] + 1]
            elif H[0] < T[0] and H[1] < T[1]:
                T = [T[0] - 1, T[1] - 1]
            else:
                raise False
            if T not in seen:
                seen.append(T)
        elif abs(T[0] - H[0]) == 1 and abs(T[1] - H[1]) == 1:
            pass
        elif abs(T[0] - H[0]) + abs(T[1] - H[1]) in [1, 0]:
            pass
        else:
            T = [x + y for x, y in zip(T, d[direction])]
            if T not in seen:
                seen.append(T)


seen2 = []
rope = [[0, 0] for _ in range(10)]
H = rope[0]
seen2.append(H)
for line in lines:
    direction = line[0]
    number = int(line.split()[-1])
    for n in range(number):
        for i, T in enumerate(rope):
            if i == 0:
                H = [x + y for x, y in zip(T, d[direction])]
                rope[i] = H
            else:
                H = rope[i-1]
            if abs(H[0] - T[0]) > 0 and abs(H[1] - T[1]) > 0 and abs(T[0] - H[0]) + abs(T[1] - H[1]) in [3, 4]:
                if H[0] > T[0] and H[1] > T[1]:
                    rope[i] = [T[0] + 1, T[1] + 1]
                elif H[0] > T[0] and H[1] < T[1]:
                    rope[i] = [T[0] + 1, T[1] - 1]
                elif H[0] < T[0] and H[1] > T[1]:
                    rope[i] = [T[0] - 1, T[1] + 1]
                elif H[0] < T[0] and H[1] < T[1]:
                    rope[i] = [T[0] - 1, T[1] - 1]
                else:
                    raise False
                if i == 9 and rope[i] not in seen2:
                    seen2.append(rope[i])
            elif abs(T[0] - H[0]) == 1 and abs(T[1] - H[1]) == 1:
                pass
            elif abs(T[0] - H[0]) + abs(T[1] - H[1]) in [1, 0]:
                pass
            else:
                if H[0] > T[0] and H[1] == T[1]:
                    direction_temp = 'U'
                elif H[0] < T[0] and H[1] == T[1]:
                    direction_temp = 'D'
                elif H[0] == T[0] and H[1] > T[1]:
                    direction_temp = 'R'
                elif H[0] == T[0] and H[1] < T[1]:
                    direction_temp = 'L'
                rope[i] = [x + y for x, y in zip(T, d[direction_temp])]
                if i == 9 and rope[i] not in seen2:
                    seen2.append(rope[i])

print(f'Result 1 is: {len(seen)}')
print(f'Result 2 is: {len(seen2)}')
