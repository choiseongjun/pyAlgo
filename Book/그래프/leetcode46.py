def permute(nums):
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements)==0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            print(elements,next_elements,prev_elements)
            dfs(next_elements)
            prev_elements.pop()
    dfs(nums)
    return results

if __name__ == '__main__':
    permuteValue = [1,2,3]
    result = permute(permuteValue)
    #print(result)
