nums = [1, 2, 1, 3, 2, 5]
res = {}
for i in nums:
    if i in res:
        res.pop(i)
    else:
        res[i] = True
print(list(res.keys()))

