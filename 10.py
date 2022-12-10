import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [x.split() for x in lines]
    lines = [[x[0], int(x[1])] if len(x) > 1 else x for x in lines]

ans1 = 0
ans2 = ''
end = 220
end2 = 40 * 6
counter = 0
X = 1


def check(counter, X):
    if counter in [20, 60, 100, 140, 180, 220]:
        return counter * X
    return 0


for i in lines:
    if i[0] == 'noop':
        counter += 1
        ans1 += check(counter, X)
    else:
        counter += 1
        ans1 += check(counter, X)
        counter += 1
        ans1 += check(counter, X)
        X += i[1]
    if counter > end:
        break


def check2(counter2, X2):
    if counter2 in [X2 - 1, X2, X2 + 1]:
        return '#'
    else:
        return '.'


counter2 = 0
X2 = 1
for i in lines:
    if i[0] == 'noop':
        ans2 += check2(counter2, X2)
        counter2 += 1
        if counter2 % 40 == 0:
            X2 += 40
    else:
        ans2 += check2(counter2, X2)
        counter2 += 1
        if counter2 % 40 == 0:
            X2 += 40
        ans2 += check2(counter2, X2)
        counter2 += 1
        if counter2 % 40 == 0:
            X2 += 40
        X2 += i[1]
    if counter2 > end2:
        break

print(f'Result 1 is: {ans1}')
print(f'Result 2 is:')
for i in range(0, len(ans2), 40):
    print(ans2[i:i+40])
