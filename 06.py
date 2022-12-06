import os
import down
from collections import Counter

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    line = f.read()

d = {}

ans1 = ''
ans2 = ''
for i, ch in enumerate(line):
    if i > 2:
        a = Counter(line[i-3:i+1])
        if a[max(a, key=a.get)] == 1:
            ans1 = i + 1
            break

for i, ch in enumerate(line):
    if i > 12:
        b = Counter(line[i-13:i+1])
        if b[max(b, key=b.get)] == 1:
            ans2 = i + 1
            break

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')
