class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def factorial(n):
            if n==1 or n==0:
                return 1
            return n * factorial(n-1)
        d=dict()
        output=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d:
            if d[j]>1:
                output+=factorial(d[j])/(2*factorial(d[j]-2))
        return int(output)
