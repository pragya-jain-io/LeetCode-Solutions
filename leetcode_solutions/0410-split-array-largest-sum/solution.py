class Solution:
    def splits(self,nums,mid):
        split = 1
        sums = 0
        for i in nums:
            if i+sums>mid:
                sums=i
                split+=1
            else:
                sums+=i
        return split



    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid =(low+high)//2
            if self.splits(nums,mid) > k:
                low=mid+1
            else:
                high=mid-1
        return low
