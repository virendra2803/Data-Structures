#rank_of_array
arr = [1,1,1,2,4]
map1 = {}
res = []

arr1 = sorted(set(arr))
for i, val in enumerate(arr1):
    map1[val] = i
for i in arr:
    if i in map1:
        res.append(map1[i]+1)

print(res)