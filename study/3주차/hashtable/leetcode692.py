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
    collections.Counter(words) # 각 단어별로 집계하
    words = list(set(words)) # 셋으로 구분해서 리스트 담
    words.sort() #알파벳순으로 소팅
    words = sorted(words, key = lambda x: d[x], reverse = True)
    return words[:k]

if __name__ == '__main__':
    #Input= ["i", "love", "leetcode", "i", "love", "coding"]
    Input = ["aaa", "aa", "a"]
    k = 2
    res = topKFrequent(Input,k)
    print(res)