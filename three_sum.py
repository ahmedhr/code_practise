from typing import List


# two sum method
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    lookup = dict()

    for i, n in enumerate(nums):
        lookup[n] = i
    l = len(nums)
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue
        twosum = - n
        if i + 1 <= l:
            for j in range(i + 1, l):
                tar = twosum - nums[j]
                r = [n, nums[j], tar]
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                if tar in lookup and lookup[tar] > j:
                    ans.append(r)
    return ans


# two pointer method
def threeSum(nums: List[int]) -> List[List[int]]:
    ans = []
    ln = len(nums)
    if nums or ln < 3:
        nums.sort()
        for i, n in enumerate(nums):
            l = i + 1
            r = ln - 1
            if i > 0 and n == nums[i - 1]:
                continue
            while l < r:
                if (n + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (n + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
    return ans



lis = [-1,0,1,2,-1,-4]

print(threeSum(lis))
