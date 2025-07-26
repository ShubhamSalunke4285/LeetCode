class Solution(object):
    def maxProduct(self, nums):
        
        if not nums:
            return 0

        curr_max = curr_min = max_so_far = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max  # swap

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            max_so_far = max(max_so_far, curr_max)

        return max_so_far