def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        
        if target < nums[0]:
            return 0
        
        if target in nums:
            return nums.index(target)
        
        mitad = (len(nums))//2
        if target < nums[mitad] and target > nums[mitad-1]:
            return mitad

        if target < nums[mitad]:
            for x in range(mitad):
                if nums[x] > target:
                    return x
        else: 
             for x in range(mitad, len(nums)):
                if nums[x] > target:
                    return x
                
                     
            

lista = [1,3,5,6,8,9]
lista = [1,3]
lista = [2,3,5,6,9]
target = 7
print(searchInsert(lista, target))


'''
def searchInsert(self, nums, target):
        left, right=0 , len(nums) - 1
        while left<=right:
            mid =  (right+left) >> 1
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                left=mid+1

            else:
                 right =mid-1
        return left
'''