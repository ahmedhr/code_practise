from typing import List


def trap(height: List[int]) -> int:
    answer = 0
    for i, val in enumerate(height):
        l = 0 if i == 0 else max(height[:i])
        r = 0 if i == len(height) - 1 else max(height[i + 1:])
        answer += max(0, min(l, r) - val)

    return answer



class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        while l <= r:
            if max_left <= max_right:
                if max_left < height[l]:
                    max_left = height[l]
                    l += 1
                    continue
                ans += min(max_left, max_right) - height[l]
                l += 1

            else:
                if max_right < height[r]:
                    max_right = height[r]
                    r -= 1
                    continue
                ans += min(max_left, max_right) - height[r]
                r -= 1

        return ans
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
