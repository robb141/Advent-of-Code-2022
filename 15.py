import os
import re

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

seen = set([])
points = set()
y = 2000000

for line in lines:
    reg = r"Sensor at x=([-]?\d+).*y=([-]?\d+).*x=([-]?\d+).*y=([-]?\d+)"
    elems = re.findall(reg, line)[0]
    s1, s2, b1, b2 = int(elems[0]), int(elems[1]), int(elems[2]), int(elems[3])
    if b2 == y:
        points.add(b1)
    radius = abs(s1-b1) + abs(s2-b2)
    start = s1 - radius + abs(s2-y)
    end = s1 + radius - abs(s2-y)
    seen.update(range(start, end+1))

print(len(seen.difference(points)))


def all_numbers(s): return [int(d) for d in re.findall("(-?\d+)", s)]
def md(p, q): return abs(p[0]-q[0])+abs(p[1]-q[1])


with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read()
data = [all_numbers(line) for line in lines.split("\n")]
radius = {(a,b):md((a,b),(c,d)) for (a,b,c,d) in data}
scanners = radius.keys()

acoeffs, bcoeffs = set(), set()
for ((x,y), r) in radius.items():
    acoeffs.add(y-x+r+1)
    acoeffs.add(y-x-r-1)
    bcoeffs.add(x+y+r+1)
    bcoeffs.add(x+y-r-1)

bound = 4_000_000
for a in acoeffs:
    for b in bcoeffs:
        p = ((b-a)//2, (a+b)//2)
        if all(0<c<bound for c in p):
            if all(md(p,t)>radius[t] for t in scanners):
                print(4_000_000*p[0]+p[1])
