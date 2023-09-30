class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l=0
        h=len(nums)-1
        
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l=mid+1
            if nums[mid]>target:
                if nums[mid-1]<target:
                    return mid
                else:
                    h=mid-1
        # return len(nums)
