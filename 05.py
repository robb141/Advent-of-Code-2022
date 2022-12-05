import copy
import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

d = {}
empty_line = lines.index('')
line_len = len(lines[0])
for line in range(empty_line-2, -1, -1):
    crate_num = 1
    for crate_index in range(1, line_len, 4):
        curr = lines[line][crate_index]
        if lines[line][crate_index] == ' ':
            pass
        elif d.get(crate_num) is None:
            d[crate_num] = [curr]
        else:
            d[crate_num].append(curr)
        crate_num += 1
d1 = copy.deepcopy(d)
d2 = copy.deepcopy(d)

for line in range(empty_line+1, len(lines)):
    words = lines[line].split()
    count = int(words[1])
    source = int(words[3])
    destination = int(words[5])
    for i in range(count):
        moved = d1[source].pop()
        if d1.get(destination) is None:
            d1[destination] = [moved]
        else:
            d1[destination].append(moved)
ans1 = ''.join([d1[i][-1] for i in d1])

for line in range(empty_line+1, len(lines)):
    words = lines[line].split()
    count = int(words[1])
    source = int(words[3])
    destination = int(words[5])
    moved = d2[source][-count:]
    del d2[source][-count:]
    if d2.get(destination) is None:
        d2[destination] = [moved]
    else:
        for i in moved:
            d2[destination].append(i)
ans2 = ''.join([d2[i][-1] for i in d2])

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')
