import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [i.split(',') for i in lines]

ans1 = 0
ans2 = 0
for line in lines:
    a, b = list(map(int, line[0].split('-')))
    x, y = list(map(int, line[1].split('-')))

    if (x >= a and y <= b) or (x <= a and y >= b):
        ans1 += 1

    for i in range(a, b + 1):
        if x <= i <= y:
            ans2 += 1
            break

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')
