class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)< m*k:
            return -1
        def checkbloom(mid):
            cutk=0
            cutm=0
            for i in bloomDay:
                if i <= mid:
                    cutk+=1
                    if cutk==k:
                        cutm+=1
                        cutk=0
                    if cutm==m:
                        # print(mid,True)
                        return True
                else:
                    cutk=0

            if cutm==m:
                    # print(mid,True)
                    return True
            else:
                # print(mid,False)
                return False
        low = min(bloomDay)
        high = max(bloomDay)
        # print(low,high)
        answer  = float("inf")
        while low<=high:
            mid =(low+high)//2
            # print(low,high)
            if checkbloom(mid)==True:
                if answer > mid:
                    answer = mid
                high = mid-1
            else:
                low = mid+1
        return answer       
        


