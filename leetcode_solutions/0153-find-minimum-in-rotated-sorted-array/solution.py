class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float("inf")
        while low<=high:
            mid = (low + high)//2
            # left sorted 
            if nums[mid]>=nums[low]:
                if ans> nums[low]:
                    ans = nums[low]
                low = mid+1
            # right sorted
            else:
                if ans> nums[mid]:
                    ans = nums[mid]
                high = mid -1
        return ans



        return ans
        
