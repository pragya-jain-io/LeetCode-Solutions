class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        answer = float("inf")
        def daysNeeded(mid):
            sumw = 0
            day = 1
            for i in range(len(weights)):
                if sumw+weights[i]>mid:
                    day+=1
                    sumw = weights[i]
                else:
                    sumw+=weights[i]
            return day
         
        while low<=high:
            mid = (low+high)//2
            if daysNeeded(mid) <= days:
                if answer>mid:
                    answer = mid
                high = mid -1
            else:
                low = mid+1
        return answer


        



