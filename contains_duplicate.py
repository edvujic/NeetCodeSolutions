def contains_duplicate(nums):
    
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] == nums[j]:
                return True
    return False


print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,2,3,4,5,1]))
print(contains_duplicate([1,1,1,1,2,3,4,5,3,2,1]))