from typing import List


class Solution:
    def hIndex(self, c: List[int]) -> int:
        n = len(c)
        h = 0
        end = n - 1
        s = 0
        while (s <= end):
            m = (end + s) // 2
            if (c[m] <= (m + 1)):
                s = m + 1
                h = m + 1
            else:
                e = m - 1
        return h


s = Solution()

hin = s.hIndex([0, 1, 3, 5, 6])
print(hin)