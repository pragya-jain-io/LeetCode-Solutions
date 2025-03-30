class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)-1
        missing = 0
        answer = float("inf")
        while low<=high:
            mid = (low + high) // 2
            missing = arr[mid]-mid-1
            if missing<k:
                low = mid+1
            else:
                if answer > mid:
                    answer = mid
                high = mid-1
        print(answer)
        if answer > arr[-1]:
            return k + len(arr)
        if len(arr)==1:
            return k
        return k + answer 


