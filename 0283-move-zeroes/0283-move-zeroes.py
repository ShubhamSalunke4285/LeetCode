class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        k = 0 
        while i < len(nums)-k:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                k+=1
            else:
                i += 1
                
        