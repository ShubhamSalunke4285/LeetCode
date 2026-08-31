class Solution(object):
    def maxArea(self, height):
        left=0
        right= len(height)-1
        max_area = 0

        while left<right:
            cur_width = right-left
            cur_height = min(height[left],height[right])
            cur_area = cur_width * cur_height

            max_area = max(max_area,cur_area)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return max_area

        