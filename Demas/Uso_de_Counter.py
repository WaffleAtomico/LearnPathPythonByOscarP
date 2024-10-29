from collections  import Counter


def intersect_reto(nums1, nums2):
        # Count occurrences of each number in both lists
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        print(count1)
        print(count2)
        # Find the intersection
        intersection = count1 & count2  # This computes the minimum of counts

        # Return the result as a list
        return list(intersection.elements())
    
nums1 = [1, 22, 22, 1, 3]
nums2 = [1, 1, 22]
print(intersect_reto(nums1, nums2))