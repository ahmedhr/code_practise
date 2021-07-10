class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        keep moving the shorter line
        :param height:
        :return:
        """
        l = len(height)
        left = 0
        right = l - 1
        area = 0
        while left != right:
            if height[right] < height[left]:
                area = max(area, height[right] * (right - left))
                right -= 1
            else:
                area = max(area, height[left] * (right - left))
                left += 1
        return area


"""Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: 
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
 In this case, the max area of water (blue section) the container can contain is 49."""