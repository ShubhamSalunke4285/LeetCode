class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        target = Counter(p)
        window = {}

        k = len(p)
        result = []
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if right >= k:
                window[s[right-k]] -= 1
                if window[s[right-k]] == 0:
                    del window[s[right-k]]

            if right >= k-1:
                if target == window:
                    result.append(right-k+1)

        return result
        