
strs = ["eat","tea","ten","ate","nat","bat"]
res = ""
list = []
res = {}
for char in strs:

    word = "".join(sorted(char))
    res.setdefault(word, [])
    res[word].append(char)



print(res.values())