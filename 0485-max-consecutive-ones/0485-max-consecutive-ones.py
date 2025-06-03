class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_num = 0
        final_num = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_num += 1
                if final_num < max_num:
                    final_num = max_num
            else:
                max_num = 0
        return final_num

        