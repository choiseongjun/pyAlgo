
def arrayStringsAreEqual(word1, word2):
    res = "".join(word1)
    res1 = "".join(word2)
    check = False
    if res == res1:
        check = True
    return check




if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    arrayStringsAreEqual(word1,word2)