#!/usr/bin/python3
lines = open("day17.dat").read().splitlines()

data = set()
part2 = False
z = 0
w = 0
for y in range(len(lines)):
    for x in range(len(lines)):
        if lines[y][x] == "#":
            data.add((x,y,z,w))


def getNeig(point):
    x = point[0]
    y = point[1]
    z = point[2]
    if part2 == True:
        w = point[3]

    opt = set()
    for i in [-1,0, 1]:
        for j in [-1,0, 1]:
            for k in [-1,0, 1]:
                if part2:
                    for l in [-1,0, 1]:
                        opt.add((x+i,y+j,z+k,w+l))
                else:
                    opt.add((x+i,y+j,z+k,0))

    if part2:
        opt.remove((x,y,z,w))
    else:
        opt.remove((x,y,z,0))

    return opt

def getNeiOn(points, all):
    count = 0
    for p in points:
        if p in all:
            count+= 1
    return count

def update(d):
    newdata = set()
    allneig = set()
    for par in d:
        neig = getNeig(par)
        neigon = getNeiOn(neig, d)
        if (neigon == 2) | (neigon == 3):
            newdata.add(par)
        allneig.update(neig)
    
    for n in allneig:
        if n not in d:
            neigneig = getNeig(n)
            neigneigon = getNeiOn(neigneig,d)
            if (neigneigon == 3):
                newdata.add(n)

    return newdata

start = data
for i in range(6):
    data = update(data)
print("Part1:", len(data))

data = start
part2 = True
for i in range(6):
    data = update(data)
print("Part2:", len(data))