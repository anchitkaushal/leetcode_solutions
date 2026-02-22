class Solution:
    def isAnagram(self, s,t):
        if len(s)!=len(t):
            return False
        
        box ={}
        for ch in s:
            box[ch]=box.get(ch,0)+1
        for ch in t:
            if ch not in box:
                return False
            box[ch] -=1
        for values in box.values():
            if values != 0:
                return False
        return True
            
            
        