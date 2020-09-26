import collections

def numJewelsInStones1(j, s):
    freqs={}
    count=0

    for char in s:
        if char not in freqs:
            freqs[char]=1
        else:
            freqs[char]+=1

    for char in j:
        if char in freqs:
            count+=freqs[char]


    return count

def numJewelsInStones(j,s):
    freqs=collections.defaultdict(int)
    count=0

    for char in s:
        freqs[char]+=1

    for char in j:
        count+=freqs[char]
    return count

def CounterJwel(J,S):
    freqs=collections.Counter(S)
    count=0
    for char in J:
        count+=freqs[char]
    return count

def countpyJewl(J,S):
    return sum(s in J for s in S)
j="aA"
s="aAAbbbb"
#print(numJewelsInStones(j,s))
#print(numJewelsInStones1(j,s))
print((CounterJwel(j,s)))