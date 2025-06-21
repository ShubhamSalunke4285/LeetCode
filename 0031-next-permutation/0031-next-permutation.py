class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find the pivot (first decreasing element from right)
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the next larger element from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the subarray from i+1 to end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        