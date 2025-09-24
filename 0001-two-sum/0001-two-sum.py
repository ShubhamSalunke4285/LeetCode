class Solution(object):
    def twoSum(self, nums, target):
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return i,j
        
        hashmap = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i