#p1 - Two Sum

nums = [2,7,11,15]
target = 17

class Solution(object):
    def twoSum( self, nums, target):
        hash_map = {}

        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i
        return []
    print(twoSum(nums,target))