def merge(nums1, m, nums2, n):
        resp =[]
        i = 0
        j = 0
        if m == 0:
            return nums2[0:n]
        if n == 0:
            return nums1[0:m]
        while m > 0 or n > 0:
            if nums1[i] <= nums2[j] and m != 0:
                resp.append(nums1[i])
                m = m-1
                
            if nums2[j] >= nums1[i] and n !=0:
                resp.append(nums2[j])
                n = n-1
            i=i+1   
            j=j+1
        return resp
        
       
nums1 = [1,2,3,0,0,0]
# nums1 = [1, 2]
m = 3
num2 = [2,5,6]
# num2 = []
n = 3
r = merge(nums1, m, num2, n)
print(r)



'''
if m > 0:
            resp += nums1[0:m]
        if n > 0:
            resp += nums2[0:n]
'''