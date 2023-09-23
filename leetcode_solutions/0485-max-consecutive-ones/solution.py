class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            if i==0:
                if max < count: 
                    max = count
                count=0
            
        if max < count:
            max = count
        return max
