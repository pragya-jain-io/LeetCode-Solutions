class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:
        def check_single(nums,mid):
            if mid > 0:
                if nums[mid-1]==nums[mid]:
                    return False
            if mid < len(nums) - 1:
                if nums[mid+1]==nums[mid]:
                    return False
            return True
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high) //2
            # checK single
            if check_single(nums,mid):
                return nums[mid]
            else:
                if nums[mid+1]==nums[mid]:
                    pix = mid + 1
                    if (high - pix) % 2 != 0:
                        low = pix + 1
                    else: 
                        high = mid - 1
                else:
                    pix = mid - 1
                    if (high - mid) % 2 != 0:
                        low = mid + 1
                    else: 
                        high = pix - 1

                


