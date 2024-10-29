def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    n_elim = nums.count(val)
    for x in range(n_elim):
        nums.remove(val)
        

'''
i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
'''