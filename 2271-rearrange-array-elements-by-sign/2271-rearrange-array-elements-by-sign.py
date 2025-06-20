class Solution(object):
    def rearrangeArray(self, nums):
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res


        