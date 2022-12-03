import os
import down


def calc_ans(chars):
    ans = 0
    for letter in chars:
        if letter.islower():
            ans += ord(letter) - 96
        else:
            ans += ord(letter) - 64 + 26
    return ans


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

letters = []
for line in lines:
    second_half = line[len(line)//2:]
    for index in range(len(line) // 2):
        if line[index] in second_half:
            letters.append(line[index])
            break

ans1 = calc_ans(letters)

letters2 = []
for i, line in enumerate(lines):
    if (i+1) % 3 == 0:
        for ch in line:
            if ch in lines[i-1] and ch in lines[i-2]:
                letters2.append(ch)
                break
    else:
        continue

ans2 = calc_ans(letters2)

print(f'Result 1 is: {ans1}')
print(f'Result 2 is: {ans2}')
