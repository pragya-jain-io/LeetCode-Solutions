class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # max=0
        n=len(nums)
        sum=0
        for i in nums:
            sum+=i
            # if i>max:
            #     max=i
        n=(n*(n+1))/2
        return int(n-sum)
        
