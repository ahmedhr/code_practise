from typing import List


def findRestaurant(l1: List[str], l2: List[str]) -> List[str]:
    d2 = {l2[i]: i for i in range(len(l2))}
    res = {}
    for i in range(len(l1)):
        val = l1[i]
        if val in d2:
            res[i + d2[val]] = res.get((i + d2[val]), [])
            res[i + d2[val]].append(val)
    for i in sorted(res):
        return res[i]


a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
b = ["KFC", "Shogun", "Burger King"]

findRestaurant(a, b)
