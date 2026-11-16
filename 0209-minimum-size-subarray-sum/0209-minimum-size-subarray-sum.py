class Solution(object):
    def minSubArrayLen(self, target, nums):
        left =0
        min_len = float("inf")
        curr_len =0

        for right in range(len(nums)):
            curr_len += nums[right]

            while curr_len >= target:
                min_len = min(min_len, right-left+1)
                
                curr_len -= nums[left]
                left += 1
        
        return 0 if min_len == float("inf") else min_len

        