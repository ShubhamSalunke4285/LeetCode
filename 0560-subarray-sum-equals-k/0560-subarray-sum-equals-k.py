class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # base case

        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1

        return count





        