import collections
# def numJewelsInStones(j, s):
#     freqs={}
#     count=0
#
#     for char in s:
#         if char not in freqs:
#             freqs[char]=1
#         else:
#             freqs[char]+=1
#
#     for char in j:
#         if char in freqs:
#             count+=freqs[char]
#
#
#     return count

def numJewelsInStones(j,s):
    freqs=collections.defaultdict(int)
    count=0

    for char in s:
        freqs[char]+=1

    for char in j:
        count+=freqs[char]
    return count


j="aA"
s="aAAbbbb"
print(numJewelsInStones(j,s))