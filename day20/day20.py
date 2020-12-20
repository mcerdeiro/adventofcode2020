#!/usr/bin/python3
from itertools import product
from copy import deepcopy

lines = open("day20.dat").read().splitlines()

data = []
tile = None
tiles = {}

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

def get(x,y):
    for k,v in withpositions.items():
        if(v["pos"] == (x,y)):
            return k

    return None

def countNei(k):
    #print("Counting nei", k)
    count = 0
    p = withpositions[k]["pos"]
    pos = [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]
    for p in pos:
        if get(p[0], p[1]) != None:
            count += 1

    return count


def tryToFlip(k):
    neicount = countNei(k)
    #print("Nei", neicount)
    if neicount == 1:
        #print("Trying to flip", k)
        v = withpositions.pop(k)
        tiles[k] = v

    return True

def tryToPos(k, pos, side, v1):
    k2 = k
    ret = False
    #printState()
    #print("Try to pos", k, "in", pos, "side", 3)
    #print("side", side, "side new", i.index(v1["rf"][side]))
    offset = - (side + 2)%4 + i.index(v1["rf"][side])
    rf = (i[(offset+0)%4], i[(offset+1)%4], i[(offset+2)%4], i[(offset+3)%4])
    #print("rf", rf)
    up = get(pos[0], pos[1]-1)
    down = get(pos[0], pos[1]+1)
    right = get(pos[0]+1, pos[1])
    left = get(pos[0]-1, pos[1])

    correct = True
    if up != None:
        if withpositions[up]["rf"][2] != rf[0]:
            #print("not possible up", up, "not comp with", rf[0], "not compatible with", withpositions[up]["rf"][2])
            correct = False
        else:
            #print("up compatible")
            pass
    if down != None:
        #print("down", down, withpositions[down])
        if withpositions[down]["rf"][0] != rf[2]:
            #print("not possible down", down, "value", rf[2], "not compatible with", withpositions[down]["rf"][0])
            correct = False
        else:
            #print("down compatible")
            pass
    if left != None:
        if withpositions[left]["rf"][1] != rf[3]:
            #print("not possible left", left, "not comp with", rf[3], "not compatible with", withpositions[left]["rf"][1])
            #tryToFlip(left, "left")
            correct = False
        else:
            #print("left compatible")
            pass
    if right != None:
        if withpositions[right]["rf"][3] != rf[1]:
            #print("not possible right", right, "not comp with", rf[1], "not compatible with", withpositions[right]["rf"][3])
            correct = False
        else:
            #print("right compatible")
            pass
    
    if correct == True:
        #print("Correct")
        withpositions[k2] = v2
        withpositions[k2]["pos"] = newpos
        withpositions[k2]["rf"] = rf
        tiles.pop(k2)
        ret = True
    else:
        #printState()
        #print("Not possible", k, pos, v1["pos"], get(v1["pos"][0], v1["pos"][1]))
        #print("k", k, tiles[k])
        #print("other", get(v1["pos"][0], v1["pos"][1]), v1)
        for k in [up, right, down, left]:
            if k != None:
                #print("Try to flip", k)
                if tryToFlip(k):
                    return True
    
    #printState()
    #input("new")
    return ret

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

def getBinary(message):
    #ret = (int(message.replace(".","0").replace("#","1"),2), int(message.replace(".","1").replace("#","0"),2))
    binary = message.replace(".","0").replace("#","1")
    ret = (int(binary,2), int(binary[::-1],2))
    #print(message, ret)
    return ret



for k,v in tiles.items():
    #print("checking", k)
    top = getBinary(v["data"][0])
    bottom = getBinary(v["data"][len(v["data"])-1])
    fcol = ""
    lcol = ""
    for y in range(len(v["data"])):
        fcol += v["data"][y][0]
        lcol += v["data"][y][len(v["data"][y])-1]
    right = getBinary(lcol)
    left = getBinary(fcol)
    options = []
    options.append(top)
    options.append(right)
    options.append(bottom)
    options.append(left)
    tiles[k]["n"] = options

    rot = []
    rot.append((top[0],right[0],bottom[0],left[0])) # original
    rot.append((left[1],top[0],right[1],bottom[0])) # rotate 1
    rot.append((bottom[1],left[1],top[1],right[1])) # rotate 2
    rot.append((right[1],bottom[1],left[0],top[1])) # rotate 3
    #original flipped vertival
    rot.append((bottom[0],right[1],top[0],left[1])) # flipped vertival
    #original flipped horizontal
    rot.append((top[1],left[0],bottom[1],right[0])) # flipped horizonatl
    #first rotation flipped vertical
    rot.append((right[1],top[1],left[1],bottom[1])) # rotate 1 flipped vertical
    #first rotation flipped horizontal
    rot.append((left[0],bottom[0],right[0],top[0])) # rotate 1 flipped horizontal
    


    tiles[k]["r"] = rot

#print(tiles[3079])


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

def rotate(image):
    newimage = []
    for x in range(len(image[0])):
        line = ""
        for y in range(len(image)-1,-1,-1):
            #print(x,y, len(image), len(image[y]), image[y])
            line += image[y][x]
        newimage.append(line)

    assert(len(image) == len(newimage))
    assert(len(image[0]) == len(newimage[0]))

    return newimage

def flipHor(image):
    newimage = []
    for y in range(len(image)):
        newimage.append(image[y][::-1])

    assert(len(image) == len(newimage))
    assert(len(image[0]) == len(newimage[0]))
    return newimage

def flipVer(image):
    newimage = []
    for y in range(len(image)-1,-1,-1):
        newimage.append(image[y])

    assert(len(image) == len(newimage))
    assert(len(image[0]) == len(newimage[0]))

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
    #print("Try to pos", k1, k2)
    #print("In board", withpositions[k1])
    #print("New", tiles[k2])
    found = 0
    foundr = None
    founddir = None
    for i in range(len(v1["rf"])):
        #print("Checking side", i, v1["rf"][i])
        ci = [2, 3, 0, 1][i]
        for r in v2["r"]:
            if v1["rf"][i] == r[ci]:
                found += 1
                foundr = r
                founddir = ci
                #print("Found")

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
        
        #print("Found", v1["rf"], foundr, founddir)
        #print("Pos original", v1["pos"], "new pos", p)

        withpositions[k2] = v2
        withpositions[k2]["pos"] = p
        withpositions[k2]["rf"] = foundr
        tiles.pop(k2)

        #input("foo")

        return True

    return False


cont = True
withpositions = dict()
k = list(tiles.keys())[0]
withpositions[k] = tiles[k]
withpositions[k]["pos"] = (0,0)
withpositions[k]["rf"] = withpositions[k]["r"][0]
tiles.pop(k)
#print("k", k)
#print(tiles[3079])

while len(tiles) != 0:
    #print("len", len(tiles))
    if len(tiles) == 1:
        #printState()
        #print(tiles)
        #input("foo")
        pass
    
    found = False
    for k1,v1 in withpositions.items():
        #printState()
        #print("Checking", k1)
        for k2, v2 in tiles.items():
            #print("Checking if compatible with", k2)
            if checkAndPos(k1,k2):
                found = True
                break
            # if k1 == k2:
            #     assert(0)
            # for side in range(4):
            #     #print("Checking", side, v1["rf"][side])
            #     #print(v2["r"])
            #     for i in v2["r"]:

                        
            #         if v1["rf"][side] in i:
            #             print("match k", k1, "with k", k2, "in", v1["rf"][side], i, side)
            #             #print(v1["rf"][side], side, v1["rf"], k1)
            #             if side == 3:
            #                 newpos = (v1["pos"][0]-1, v1["pos"][1])
            #             elif side == 0:
            #                 newpos = (v1["pos"][0], v1["pos"][1]-1)
            #             elif side == 1:
            #                 newpos = (v1["pos"][0]+1, v1["pos"][1])
            #             elif side == 2:
            #                 newpos = (v1["pos"][0], v1["pos"][1]+1)
            #             else:
            #                 assert(0)
            #             if tryToPos(k2, newpos, side, v1) == True:
            #                 found = True
            #                 break
            #     if found == True:
            #         break        
            if found == True:
                break            
        if found == True:
            break            
#print("sii3", len(withpositions), len(tiles))
# for k,v in withpositions.items():
#     print("Positions", v["pos"])


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

#printState()
#print(vals[0], vals[1], vals[2], vals[3])
print("Part1:",vals[0] * vals[1] * vals[2] * vals[3])


#remove not needed data
X = 0
Y = 0
for k,v in withpositions.items():
    v["data"] = v["data"][1:-1]
    for i in range(len(v["data"])):
        v["data"][i] = v["data"][i][1:-1]
        rotindex = v["r"].index(v["rf"])
    v["data"] = rotateFlip(v["data"], rotindex)
    Y = len(v["data"])
    X = len(v["data"][0])

#print(minx, maxx, miny, maxy)

fullimage = []
for y in range(miny, maxy+1):
    for y2 in range(Y):
        line = ""
        for x in range(minx, maxx+1):
            for k,v in withpositions.items():
                if v["pos"] == (x,y):
                    line += v["data"][y2]
        fullimage.append(line)

def findMonster(image):
    total = 0
    count = 0
    pattern = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
    #"..................#."
    #"#....##....##....###",
    #".#..#..#..#..#..#...",
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

original = deepcopy(fullimage)

# fullimage = rotateFlip(fullimage, 1)
# monsters = findMonster(fullimage)
# print("Monster", monsters)
# print("Part2:", countOn(fullimage) - monsters * 15)
# exit()

total = countOn(fullimage)

backup = deepcopy(fullimage)

for i in range(8):
    fullimage = deepcopy(backup)
    fullimage = rotateFlip(fullimage, i)
    monsters = findMonster(fullimage)
    if monsters != 0:
        print("Part2:", total - monsters * 15)
        exit()






                


    