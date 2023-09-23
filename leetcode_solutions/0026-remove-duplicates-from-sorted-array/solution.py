class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for e in range(len(nums)):
            if nums[i]!=nums[e]:
                i+=1
                nums[i]=nums[e]
            else:
                continue
                
        return i+1


