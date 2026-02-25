class Solution:
    def sortArray(self, nums):
        # Base case
        if len(nums) <= 1:
            return nums
        
        # Divide
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # Merge
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        result = []
        i = j = 0
        
        # Compare and merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining
        result += left[i:]
        result += right[j:]
        
        return result
        