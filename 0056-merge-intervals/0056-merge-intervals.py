class Solution(object):
    def merge(self, intervals):
        # op = intervals
        # op.sort()
        # n = len(intervals)
        # i = 0
        # while i < n-1:
        #     if intervals[i][0] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]:
        #         op.pop(i)
        #         n-=1
        #     elif intervals[i][0] <= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][1]:
        #         op.pop(i+1)
        #         n-=1
        #     elif intervals[i][1] >= intervals[i+1][0]:
        #         op[i] = [intervals[i][0],intervals[i+1][1]]
        #         op.pop(i+1)
        #         n-=1
        #     elif intervals[i][1] < intervals[i+1][0]:
        #         i+=1
        # return op

        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

        