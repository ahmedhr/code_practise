from typing import List


class Solution:
    def hIndex(self, c: List[int]) -> int:
        n = len(c)
        h = 0
        c.sort(reverse=True)
        for i in range(n):
            if i+1 <= c[i]:
                h = i+1
        return h


s = Solution()

hin = s.hIndex([3, 0, 6, 1, 5])
print(hin)
