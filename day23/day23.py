#!/usr/bin/python3

inp = "792845136"

def getFollows(i, data):
  pos = data.index(str(i))
  pos = (1 + pos) %  len(data)
  return int(data[pos])
  
def printData(data, pos):
  tmp = ""
  tmp += "(" + str(pos) + ") "
  pos = data[pos-1]
  for i in range(len(data)-1):
    tmp += str(pos) + " "
    pos = data[pos-1]
  print(tmp)

def getNextDest(data, pos, M):
  nd = pos-1
  n1 = getNext(data, pos)
  n2 = getNext(data, n1)
  n3 = getNext(data, n2)
  if nd == 0:
    nd = M-1
  while nd in [n1, n2, n3]:
    nd -= 1
    if nd == 0:
      nd = M-1

  assert(nd != 0)
  return nd

def getNext(data, pos):
  p = (pos - 1) % len(data)
  return data[p]

def move(data, pos, M):
  nd = getNextDest(data, pos, M)
  n1 = getNext(data, pos)
  n2 = getNext(data, n1)
  n3 = getNext(data, n2)
  n4 = getNext(data, n3)
  ndn = getNext(data, nd)

  data[nd-1] = n1
  data[n3-1] = ndn
  data[pos-1] = n4
  
  return n4

def solve(inp, part2 = False):
  data = []
  M = 0

  for i in range(len(inp)):
    follows = getFollows(i+1, inp)
    data.append(follows)
    M = max(M, follows+1)

  if part2:
    for i in range(len(inp)+1, 1000000+1):
      follows = i+1
      data.append(follows)
      M = max(M, follows)

    data[int(inp[-1])-1] = 10
    data[-1] = int(inp[0])

  pos = int(inp[0])
  steps = 100
  if part2:
    steps = 10000000
  for i in range(steps):
    pos = move(data,pos, M)
  
  if part2:
    return data[0] * data[data[0]-1]
  else:
    tmp = ""
    next = 1
    for i in range(8):
      next = data[next-1]
      tmp += str(next)
    return tmp


ans1 = solve(inp, False)
print("Part1:", ans1)

ans2 = solve(inp, True)
print("Part2:", ans2)
