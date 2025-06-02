class Solution(object):
    def missingNumber(self, nums):
        # for i in range(len(nums)+1):
        #     if i in nums:
        #         continue
        #     else:
        #         return i
        
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)