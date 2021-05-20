import collections
import heapq

# def topKFrequent(words, k):
#     reversed(words)
#
#     print(reversed(words))
#     cnt = collections.Counter(words).most_common(k)
#     # sorted(cnt,reverse=False)
#     li=[]
#     for i in cnt:
#         li.append(i[0])
#     print(li)
#
#     return li
def topKFrequent( words, k: int):
    d = collections.Counter(words) # count the frequency of each word
    words = list(set(words)) # form the list with unique words
    print(words)
    words.sort() #first sort it by alphabetical order
    words = sorted(words, key = lambda x: d[x], reverse = True) #then sort it by frequency in reverse order
    return words[:k]

if __name__ == '__main__':
    #Input= ["i", "love", "leetcode", "i", "love", "coding"]
    Input = ["aaa", "aa", "a"]
    k = 2
    res = topKFrequent(Input,k)
    print(res)