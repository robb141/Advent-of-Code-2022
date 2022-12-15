import os
import down
from collections import defaultdict

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

path = []
S = defaultdict(int)
for line in lines:
    words = line.strip().split(' ')
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[0] == 'dir':
        continue
    elif words[1] == 'ls':
        continue
    else:
        sz = int(words[0])
        for i in range(1, len(path)+1):
            S['/'.join(path[:i])] += sz

total = 70000000 - max(S.values())
needed = 30000000 - total
ans1 = 0
ans2 = 0
smallest = float('inf')
for k, v in S.items():
    if v < 100000:
        ans1 += v
    if v > needed:
        diff = v - needed
        if diff < smallest:
            smallest = diff
            ans2 = S[k]

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')

