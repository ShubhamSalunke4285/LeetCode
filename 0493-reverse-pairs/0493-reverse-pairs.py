class Solution:
    def reversePairs(self, nums):
        def merge_sort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)

            # Count reverse pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge step
            temp = []
            l, r = left, mid + 1
            while l <= mid and r <= right:
                if nums[l] <= nums[r]:
                    temp.append(nums[l])
                    l += 1
                else:
                    temp.append(nums[r])
                    r += 1
            while l <= mid:
                temp.append(nums[l])
                l += 1
            while r <= right:
                temp.append(nums[r])
                r += 1

            nums[left:right+1] = temp
            return count

        return merge_sort(0, len(nums) - 1)