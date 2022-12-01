import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    res1 = 0
    semicount = 0
    cals = []
    for cal in lines:
        if cal == '':
            cals.append(semicount)
            semicount = 0
        else:
            semicount += int(cal)
    res1 = max(cals)
    res2 = sum(sorted(cals)[-3:])
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
