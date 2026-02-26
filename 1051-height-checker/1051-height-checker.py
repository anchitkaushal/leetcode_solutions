class Solution:
    def heightChecker(self, heights):
        nums = sorted(heights)
        count = 0
        for i in range(len(heights)):
           if heights[i]!=nums[i]:
             count+=1
        return count
        