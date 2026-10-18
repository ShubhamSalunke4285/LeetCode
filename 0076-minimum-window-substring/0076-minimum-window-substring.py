class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(t)>len(s):
            return ""

        need={}
        for char in t:
            need[char]= need.get(char, 0) + 1

        left = 0
        minlength = float("inf")
        start = 0
        window = {}
        target = len(need)
        goal = 0

        for right, char in enumerate(s):
            window[char]= window.get(char,0) + 1

            if char in need and window[char] == need[char]:
                goal+=1

            while goal == target:
                currlength = right-left+1

                if currlength < minlength:
                   minlength = currlength
                   start = left

                leftchar = s[left]
                window[leftchar] -= 1 
                
                if leftchar in need and window[leftchar] < need[leftchar]:
                    goal-=1

                left += 1

        if minlength == float("inf"):
            return ""
        
        return s[start: start+minlength]




        