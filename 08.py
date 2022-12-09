import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()


def vertical(start, end):
    temp = 0
    step = 1 if start < end else -1
    for k in range(start, end, step):
        if lines[i][j] <= lines[k][j]:
            temp += 1
            break
        elif lines[i][j] > lines[k][j]:
            temp += 1
    return temp


def horizontal(start, end):
    temp = 0
    step = 1 if start < end else -1
    for k in range(start, end, step):
        if lines[i][j] <= lines[i][k]:
            temp += 1
            break
        elif lines[i][j] > lines[i][k]:
            temp += 1
    return temp


ans2 = 0
ans1 = len(lines) * 2 + len(lines[0]) * 2 - 4
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-1):
        if all(lines[i][j] > lines[i-k][j] for k in range(1, i+1)) or \
            all(lines[i][j] > lines[i+k][j] for k in range(1, len(lines[i])-i)) or \
                all(lines[i][j] > lines[i][j-k] for k in range(1, j+1)) or \
                all(lines[i][j] > lines[i][j+k] for k in range(1, len(lines)-j)):
            ans1 += 1

for i in range(1, len(lines)-1):
    for j in range(1, len(lines[i])-1):
        temp_ans = vertical(i - 1, -1)
        if temp_ans == 0:
            continue
        temp_ans *= vertical(i + 1, len(lines[i]))
        if temp_ans == 0:
            continue
        temp_ans *= horizontal(j - 1, -1)
        if temp_ans == 0:
            continue
        temp_ans *= horizontal(j + 1, len(lines))
        ans2 = max(ans2, temp_ans)


print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')
