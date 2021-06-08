import math
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    l = len(nums)
    s = 0
    start = 0
    ans = math.inf
    for i in range(l):
        s += nums[i]
        while s >= target:
            res = (i + 1) - start
            s -= nums[start]
            start += 1
            ans = min(res, ans)
    print(ans)


num = [2, 3, 1, 2, 4, 3]
tar = 2
minSubArrayLen(tar, num)
