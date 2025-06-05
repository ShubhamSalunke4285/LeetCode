class Solution(object):
    def singleNumber(self, nums):
        # result = 0
        # for num in nums:
        #     result ^= num  # Apply XOR step-by-step
        # return result
        return 2*sum(set(nums))-sum(nums)
        


        