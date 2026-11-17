class Solution(object):
    def checkInclusion(self, s1, s2):
        left = 0
        target = Counter(s1)
        window = {}
        k = len(s1)

        for right, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1

            if right >= k:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if right >= k-1:
                if window == target:
                    return True 
        
        return False