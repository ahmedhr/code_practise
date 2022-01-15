def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    zi = None
    repl = 1
    for i in range(l):
        if nums[i] == 0 and repl:
            zi = i
            repl = 0
        elif nums[i] != 0:
            if zi is not None:
                nums[zi], nums[i] = nums[i], nums[zi]
                repl = 1
                if zi + 1 < l:
                    if nums[zi + 1] == 0:
                        zi = zi + 1
                        repl = 0

    return nums


# print(moveZeroes([0, 0, 1, 0, 2, 0, 0, 0, 0, 0]))

# Single pointer

def moveZeroes(nums) -> list:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero = None
    i = 0
    while i < len(nums):
        if nums[i] != 0 and zero is not None:
            nums[zero], nums[i] = nums[i], nums[zero]
            i = zero
            zero = None
        elif nums[i] == 0 and zero is None:
            zero = i
        i += 1

    return nums


print(moveZeroes([0, 0, 1, 0, 2, 0, 0, 0, 0, 0]))

# Two pointers 
# O(n)
def moveZeroes(nums) -> list:
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j = 0, 0
    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        if nums[i] != 0:
            i += 1
        if nums[j] == 0:
            j += 1

    return nums


print(moveZeroes([0, 0, 1, 0, 2, 0, 0, 0, 0, 0]))
