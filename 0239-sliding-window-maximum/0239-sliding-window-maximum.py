class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        output = []

        for right in range(len(nums)):
            while dq and dq[0] <= right - k :
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            if right >= k-1:
                output.append(nums[dq[0]])
        return output


        