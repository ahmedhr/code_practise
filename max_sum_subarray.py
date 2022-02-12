
# O(n)
# Kandane's Algorithm
# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
def maxSubArray(nums):
    a = s = nums[0]
    for i in range(1, len(nums)):
        a += nums[i]
        s = max(s, a)
        if a < 0: a = 0
    return s


print(maxSubArray([1, 4, 8, 9, -1]))
