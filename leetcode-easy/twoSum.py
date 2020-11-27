# Two Sum
def twoSum(nums, target):
    # Using Dictionary
    myDictionary = dict()
    for i in range(len(nums)):
        t = target - nums[i]
        if nums[i] in myDictionary:
            return [myDictionary[nums[i]],i]
        else:
            myDictionary[t] = i

    #Brute Force
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            mySum = nums[i] + nums[k]
            if mySum == target:
                return [i, k]
# print(twoSum([3,2,3], 6))