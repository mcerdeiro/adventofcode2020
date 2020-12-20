#!/usr/bin/python3
from itertools import product
from copy import deepcopy

lines = open("day20.dat").read().splitlines()

# used only for debugging to print the state of the map
def printState():
    R = 5
    for y in range(-R, R, 1):
        before = ""
        line = ""
        after = ""
        for x in range(-R, R, 1):
            for k,v in withpositions.items():
                if (v["pos"][0] == x) & (v["pos"][1] == y):
                    before += "        " + str(v["rf"][0]) + "       "
                    line += " . " + str(v["rf"][3]) + "-" + str(k) + "-" + str(v["rf"][1]) + " . "
                    after +=  "        " + str(v["rf"][2]) + "       "

        print(before)
        print(line)
        print(after)

# Get the binary representation of the side read in both direcations (for flipping)
def getBinary(message):
    binary = message.replace(".","0").replace("#","1")
    ret = (int(binary,2), int(binary[::-1],2))
    return ret

# process input
# read all input into data
data = []
tiles = {}
tile = None
for line in lines:
    if line.startswith("Tile "):
        if tile != None:
            tiles[tile] =  {}
            tiles[tile]["data"] = data
        data = []
        tile = int(line.split()[1][0:-1])
    else:
        if line != "":
            data.append(line)

for k,v in tiles.items():
    top = getBinary(v["data"][0])
    bottom = getBinary(v["data"][len(v["data"])-1])
    fcol = ""
    lcol = ""
    for y in range(len(v["data"])):
        fcol += v["data"][y][0]
        lcol += v["data"][y][len(v["data"][y])-1]
    right = getBinary(lcol)
    left = getBinary(fcol)

    # Possible rotations. D are dupplicated so not needed. Total 8
    #
    # 123 741 987 369
    # 456 852 654 258
    # 789 963 321 147
    #
    #          D   D
    # 789 963 321 147
    # 456 852 654 258
    # 123 741 987 369
    #          D   D
    # 321 147 789 963
    # 654 258 456 852
    # 987 369 123 741
    #
    #  D   D   D   D
    # 987 369 123 741
    # 654 258 456 852
    # 321 147 789 963

    rot = []
    rot.append((top[0],right[0],bottom[0],left[0])) # original
    rot.append((left[1],top[0],right[1],bottom[0])) # rotate 1
    rot.append((bottom[1],left[1],top[1],right[1])) # rotate 2
    rot.append((right[1],bottom[1],left[0],top[1])) # rotate 3
    rot.append((bottom[0],right[1],top[0],left[1])) # flipped vertival
    rot.append((top[1],left[0],bottom[1],right[0])) # flipped horizonatl
    rot.append((right[1],top[1],left[1],bottom[1])) # rotate 1 flipped vertical
    rot.append((left[0],bottom[0],right[0],top[0])) # rotate 1 flipped horizontal
    tiles[k]["r"] = rot

def rotate(image):
    newimage = []
    for x in range(len(image[0])):
        line = ""
        for y in range(len(image)-1,-1,-1):
            line += image[y][x]
        newimage.append(line)

    return newimage

def flipHor(image):
    newimage = []
    for y in range(len(image)):
        newimage.append(image[y][::-1])

    return newimage

def flipVer(image):
    newimage = []
    for y in range(len(image)-1,-1,-1):
        newimage.append(image[y])

    return newimage


def rotateFlip(image, index):
    newimage = []
    # 0 -> original
    # 1 -> rotate 1
    # 2 -> rotate 2
    # 3 -> rotate 3
    # 4 -> flipped vertival
    # 5 -> flipped horizonatl
    # 6 -> rotate 1 flipped vertical
    # 7 -> rotate 1 flipped horizontal
    if index == 0:
        newimage = image
    elif index == 1:
        newimage = rotate(image)
    elif index == 2:
        newimage = rotate(image)
        newimage = rotate(newimage)
    elif index == 3:
        newimage = rotate(image)
        newimage = rotate(newimage)
        newimage = rotate(newimage)
    elif index == 4:
        newimage = flipVer(image)
    elif index == 5:
        newimage = flipHor(image)
    elif index == 6:
        newimage = rotate(image)
        newimage = flipVer(newimage)
    elif index == 7:
        newimage = rotate(image)
        newimage = flipHor(newimage)
    
    return newimage

def checkAndPos(k1, k2):
    v1 = withpositions[k1]
    v2 = tiles[k2]
    found = 0
    foundr = None
    founddir = None
    for i in range(len(v1["rf"])):
        ci = [2, 3, 0, 1][i]
        for r in v2["r"]:
            if v1["rf"][i] == r[ci]:
                found += 1
                foundr = r
                founddir = ci

    assert(found <= 1)
    if found >= 1:
        p = v1["pos"]
        if founddir == 0:
            p = (p[0], p[1]+1)
        elif founddir == 1:
            p = (p[0]-1, p[1])
        elif founddir == 2:
            p = (p[0], p[1]-1)
        elif founddir == 3:
            p = (p[0]+1, p[1])
        else:
            assert(0)

        withpositions[k2] = v2
        withpositions[k2]["pos"] = p
        withpositions[k2]["rf"] = foundr
        tiles.pop(k2)

        return True

    return False

def findMonster(image):
    count = 0
    pattern = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   ",
    ]
    for y in range(len(image)-len(pattern)):
        for x in range(len(image[0])-len(pattern[0])):
            found = True
            for y1 in range(len(pattern)):
                for x1 in range(len(pattern[0])):
                    if pattern[y1][x1] == "#":
                        if image[y+y1][x+x1] != "#":
                            found = False
                if found == False:
                   break
            if found == True:
                count += 1

    return count

def countOn(image):
    count = 0
    for y in range(len(image)):
        count += image[y].count("#")

    return count

cont = True
withpositions = dict()

# the first tile is used as referenced and entered manually
# all others will be adapted based on the first one
k = list(tiles.keys())[0]
withpositions[k] = tiles[k]
withpositions[k]["pos"] = (0,0)
withpositions[k]["rf"] = withpositions[k]["r"][0]
tiles.pop(k)

while len(tiles) != 0:
    found = False
    for k1,v1 in withpositions.items():
        for k2, v2 in tiles.items():
            if checkAndPos(k1,k2):
                found = True
                break
            if found == True:
                break            
        if found == True:
            break            

vals = []
minx = 1000
miny = 1000
maxx = -1000
maxy = -1000

for k,v in withpositions.items():
    minx = min(v["pos"][0], minx)
    miny = min(v["pos"][1], miny) 
    maxx = max(v["pos"][0], maxx)
    maxy = max(v["pos"][1], maxy) 

for k,v in withpositions.items():
    if v["pos"] == (minx, miny):
        vals.append(k)
    if v["pos"] == (minx, maxy):
        vals.append(k)
    if v["pos"] == (maxx, maxy):
        vals.append(k)
    if v["pos"] == (maxx, miny):
        vals.append(k)

print("Part1:",vals[0] * vals[1] * vals[2] * vals[3])


#remove not needed data
Y = None
for k,v in withpositions.items():
    v["data"] = v["data"][1:-1]
    for i in range(len(v["data"])):
        v["data"][i] = v["data"][i][1:-1]
        
    # rotate and floip to the right position
    rotindex = v["r"].index(v["rf"])
    v["data"] = rotateFlip(v["data"], rotindex)
    if Y == None:
        Y = len(v["data"])

fullimage = []
for y in range(miny, maxy+1):
    for y2 in range(Y):
        line = ""
        for x in range(minx, maxx+1):
            for k,v in withpositions.items():
                if v["pos"] == (x,y):
                    line += v["data"][y2]
        fullimage.append(line)

original = deepcopy(fullimage)

total = countOn(fullimage)

backup = deepcopy(fullimage)

for i in range(8):
    fullimage = deepcopy(backup)
    fullimage = rotateFlip(fullimage, i)
    monsters = findMonster(fullimage)
    if monsters != 0:
        print("Part2:", total - monsters * 15)
        exit()
