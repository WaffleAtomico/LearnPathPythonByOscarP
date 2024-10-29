def merge(nums1, m, nums2, n):
    j = 0
    for x in range(0, len(nums1)):
        if nums1[x] == 0 and j <= n:
            nums1[x] = nums2[j]
            j += 1 
    nums1 = sorted(nums1)  
    return nums1
            
    
    
      
nums1 = [1,2,3,0,0,0]
# nums1 = [1, 2]
m = 3
num2 = [2,5,6]
# num2 = []
n = 3
r = merge(nums1, m, num2, n)
print(r)