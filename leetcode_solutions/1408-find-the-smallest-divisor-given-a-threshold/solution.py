import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divisor(mid):
            sum=0
            for i in nums:
                sum+=math.ceil(i/mid)
            return sum
        low = 1
        high = max(nums)
        answer = float("inf")
        while low<=high:
            mid  = (low+high)//2
            if divisor(mid)<=threshold:
                if mid<answer:
                    answer = mid
                high = mid-1
            else:
                low=mid+1
        return answer
                
                

