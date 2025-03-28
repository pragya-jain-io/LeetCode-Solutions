import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatinghours(mid):
            sum = 0
            for i in piles:
                sum += math.ceil(i / mid)
            print(sum)
            return sum
        low = 1
        high = max(piles)
        answer = float("inf")
        while low<=high:
            mid  = (low + high)//2
            if eatinghours(mid) > h:
                low=mid+1
            else:
                if mid < answer:
                    answer =  mid
                high = mid - 1
        return answer
