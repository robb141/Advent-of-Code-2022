import os
import re
import down
from copy import deepcopy

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

d = {}
monkey = 0
number = 0
for line in lines:
    if 'Monkey' in line:
        number = int(re.findall(r'\d+', line)[0])
        d[number] = {}
        d[number]['count'] = 0
    elif 'Starting' in line:
        d[number]['items'] = [int(x) for x in re.findall(r'\d+', line)]
    elif 'Operation' in line:
        d[number]['operation'] = line.split()[-3:]
    elif 'Test' in line:
        d[number]['test'] = int(re.findall(r'\d+', line)[0])
    elif 'true' in line:
        d[number]['true'] = int(re.findall(r'\d+', line)[0])
    elif 'false' in line:
        d[number]['false'] = int(re.findall(r'\d+', line)[0])

d2 = deepcopy(d)
keys = d.keys()
for _ in range(20):
    for monkey in keys:
        if len(d[monkey]['items']) == 0:
            continue
        d[monkey]['count'] += len(d[monkey]['items'])
        for item in d[monkey]['items']:
            new = eval(''.join(d[monkey]['operation']).replace('old', str(item)))
            new = new // 3
            if new % d[monkey]['test'] == 0:
                monkey_to_throw = d[monkey]['true']
                d[monkey_to_throw]['items'].append(new)
            else:
                monkey_to_throw = d[monkey]['false']
                d[monkey_to_throw]['items'].append(new)
        d[monkey]['items'] = []

sorted_counts = sorted([d[monkey]['count'] for monkey in keys])
ans1 = sorted_counts[-1] * sorted_counts[-2]

lcm = 1
for x in [d2[monkey]['test'] for monkey in keys]:
    lcm *= x

keys = d2.keys()
for _ in range(10000):
    for monkey in keys:
        if len(d2[monkey]['items']) == 0:
            continue
        d2[monkey]['count'] += len(d2[monkey]['items'])
        for item in d2[monkey]['items']:
            new = eval(''.join(d2[monkey]['operation']).replace('old', str(item)))
            new = new % lcm
            if new % d2[monkey]['test'] == 0:
                monkey_to_throw = d2[monkey]['true']
                d2[monkey_to_throw]['items'].append(new)
            else:
                monkey_to_throw = d2[monkey]['false']
                d2[monkey_to_throw]['items'].append(new)
        d2[monkey]['items'] = []

sorted_counts = sorted([d2[monkey]['count'] for monkey in keys])
ans2 = sorted_counts[-1] * sorted_counts[-2]

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')
