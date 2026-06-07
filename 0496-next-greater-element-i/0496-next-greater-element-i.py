class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                nxt_greater[smaller] = num
            stack.append(num)

        while stack:
            nxt_greater[stack.pop()] = -1
            
        ans = []
           
        for num in nums1:
            ans.append(nxt_greater[num])
            
        return ans