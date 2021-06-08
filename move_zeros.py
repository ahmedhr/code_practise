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


print(moveZeroes([0, 0, 1, 0, 2, 0, 0, 0, 0, 0]))
