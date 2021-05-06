def countMatches(items,ruleKey, ruleValue):

        arr=[]
        cnt=0
        for i in items:
            if ruleKey=="color":
                if i[1] in ruleValue:
                    arr = i
                    cnt+=1
            elif ruleKey == "type":
                if i[0] in ruleValue:
                    arr = i
            else:
                if i[2] in ruleValue:
                    arr = i
        return arr


if __name__ == '__main__':
    # items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],["phone", "gold", "iphone"]]
    # ruleKey = "color"
    # ruleValue = "silver"
    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"],
             ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    res = countMatches(items,ruleKey,ruleValue)
    print(res)