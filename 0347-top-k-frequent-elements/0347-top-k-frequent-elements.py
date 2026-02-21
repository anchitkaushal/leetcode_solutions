class Solution:
    def topKFrequent(self, nums,k):
        n2 = []
        fq = {}
        for num in nums:
            fq[num]=fq.get(num,0)+1
        for key,value in fq.items():
            n2.append((key,value))
        n2.sort(key = lambda x:x[1],reverse=True)   
        
        result = []
        for i in range(k):
            result.append((n2[i][0]))
        
        return result   
            
        