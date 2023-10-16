import os
from collections import deque

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read()
    lines = [e.split("\n") for e in lines.split("\n\n")]


def compare_ints(left, right):
    if left < right:
        return 1
    elif left > right:
        return -1
    else:
        return 0


def compare(left, right):
    i = 0
    while True:
        if 0 <= i < len(left) and 0 <= i < len(right):
            pass
        elif not (0 <= i < len(left)) and not (0 <= i < len(right)):
            return 0
        elif not (0 <= i < len(left)):
            return 1
        elif not (0 <= i < len(right)):
            return -1

        if isinstance(left[i], int) and isinstance(right[i], int):
            ret = compare_ints(left[i], right[i])
            if ret != 0:
                return ret
        else:
            lft = left[i]
            rgt = right[i]
            if isinstance(lft, int) and isinstance(rgt, list):
                lft = [lft]
            elif isinstance(lft, list) and isinstance(rgt, int):
                rgt = [rgt]
            ret = compare(lft, rgt)
            if ret != 0:
                return ret
        i += 1


ans1 = 0
count = 1
for line in lines:
    a = compare(eval(line[0]), eval(line[1]))
    if a == 1:
        ans1 += count
    count += 1


d = deque([[[2]], [[6]]])
for line in lines:
    for elem in line:
        flag_last = True
        for i, e in enumerate(d):
            if elem == '':
                flag_last = False
                break
            if compare(eval(elem), e) == 1:
                d.insert(i, eval(elem))
                flag_last = False
                break
            else:
                pass
        if flag_last:
            d.append(eval(elem))

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {(d.index([[2]])+1) * (d.index([[6]])+1)}')
