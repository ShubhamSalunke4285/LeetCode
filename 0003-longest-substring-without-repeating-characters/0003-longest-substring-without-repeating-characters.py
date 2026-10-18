class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        lastseen={}
        longest_substring=0

        for right, char in enumerate(s):
            if char in lastseen and lastseen[char] >= left:
                left = lastseen[char]+1

            lastseen[char]=right
            longest_substring = max(longest_substring,right-left+1)
        return longest_substring

        