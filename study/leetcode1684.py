def countConsistentStrings(allowed, words):

    cnt= 0
    for item in range(len(words)):
        print(words[item])
        for j in allowed:
            if j in words[item]:
                cnt+=1
            


    print(cnt)





if __name__ == '__main__':
    # allowed = "ab"
    # words = ["ad", "bd", "aaab", "baa", "badab"]
    allowed = "abc"
    words = ["a","b","c","ab","ac","bc","abc"]
    countConsistentStrings(allowed,words)