def findAnagrams(s, p):
    ans = []
    if len(s) < len(p):
        return ans
    elements_of_p = [0] * 26
    elements_of_s = [0] * 26

    for i in range(len(p)):
        elements_of_p[ord(p[i]) - ord("a")] += 1
        elements_of_s[ord(s[i]) - ord("a")] += 1


    for i in range(1, len(s) - len(p) + 1):
        # if window moves 1 to the right, the leftmost one disappears and the rightmost one is added.
        elements_of_s[ord(s[i - 1]) - ord("a")] -= 1
        elements_of_s[ord(s[i + len(p) - 1]) - ord("a")] += 1
        if elements_of_p == elements_of_s:
            ans.append(i)
    return ans



if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    findAnagrams(s,p)