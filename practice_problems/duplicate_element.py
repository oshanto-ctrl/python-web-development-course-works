def findDup(arr):
    if len(arr) < 2:
        return -1
    freq = {}
    
    freq = {x: 0 for x in arr}
    for x in arr:
        freq[x] += 1
    for k, v in freq.items():
        if v == 2:
            return k
    return -1

arr = [1, 2, 3, 3]
ans = findDup(arr)
print(ans)