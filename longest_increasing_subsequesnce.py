from cmath import inf
from typing import List


# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in nums]
        for i in range(1, len(nums)):
            j = 0
            while (j != i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], 1 + memo[j])
                j += 1
        return max(memo)

solution = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(solution)


# O(NlogN)
# Patience Sort
# refer for explanation (not the code)W
# https://www.youtube.com/watch?v=i4NBDE8ZEV8
class Solution:
    def find_first_greater(self, haystack, needle):
        low = 0
        high = len(haystack) - 1
        while low <= high:
            mid = (high + low) // 2
            if needle > haystack[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def lengthOfLIS(self, nums: List[int]) -> int:
        pile = {}
        for i in nums:
            location = self.find_first_greater(pile, i)
            pile[location] = i
        return len(pile)

solution = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
print(solution)
