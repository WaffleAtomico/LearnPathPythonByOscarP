def twoSum(nums, target):
    for x in range(len(nums)):
            fal = target - nums[x]
            try:
                if nums.index(fal) != x:
                    return [x, nums.index(fal)]
                else:
                    continue
            except ValueError:
                continue

    
def twoSum(numbers, target):
    '''
    if target % 2 != 0:
        newnumbers = list(dict.fromkeys(numbers))
    else:
        newnumbers = numbers
    '''
    newnumbers = numbers
    # print(newnumbers)
    dicc = {}
    for x in range(0, len(newnumbers)):
        for y in range(0, len(newnumbers)):
            if dicc.get((newnumbers[x] ,newnumbers[y])) and dicc.get((newnumbers[y],newnumbers[x])):
                continue   
            if (newnumbers[x] + newnumbers[y]) == target and x != y:
                return [(x+1), (y+1)]
            else:
                if x != y:
                    dicc[(newnumbers[y], newnumbers[x])] = [newnumbers[y],newnumbers[x]]
            
            
# elementos = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 0,0]
elementos = [0,0,0,0,0,0,0,0,0,0,0,0,2,3,9,9,9,9,9,9,9,9]
# elementos = [0,0,3,4]
# elementos=[2,7,11,15]
target = 9
print(twoSum(elementos, target))

#Recordar tu librito









''' 19 / 24
class Solution(object):
    def twoSum(self, numbers, target):
        dicc = {}
        for x in range(0, len(numbers)):
            for y in range(0, len(numbers)):
                if dicc.get((numbers[x] ,numbers[y])) and dicc.get((numbers[y],numbers[x])):
                    continue                
                if (numbers[x] + numbers[y]) == target and x != y:
                    return [(x+1), (y+1)]
                else:
                    if numbers[y] !=  numbers[x]:
                        dicc[(numbers[y], numbers[x] )] = [numbers[y],numbers[x]]
    
'''


''' Aceptado
for x in range(len(nums)):
            fal = target - nums[x]
            try:
                if nums.index(fal) != x:
                    return [x, nums.index(fal)]
                else:
                    continue
            except ValueError:
                continue
'''