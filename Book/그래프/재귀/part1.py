
V,E = 5,6
edges = [(1,2),(2,3),(1,4),(2,4),(1,5),(3,5)]

AM = [[0]*(V+1) for _ in range(V+1)]#1부터

for s,e in edges:
    AM[s][e] = 1
for x in AM:
    print(x)

AL = [[] for _ in range(V+1)]

for s,e in edges:
    AL[s].append(e)
for x in AL:
    print(x)


V,E = 7,8
edges = [(1,2),(1,4),(1,5),(2,3),(3,4),(3,7),(4,6),(5,6)]

AM = [[0]*(V+1) for _ in range(V+1)]

AL = [[] for _ in range(V+1)]


for s,e in edges:
    AM[s][e]=1
    AM[e][s]=1
for x in AM:
    print(x)

for s,e in edges:
    AL[s].append(e)
    AL[e].append(s)

for x in AL:
    print(x)