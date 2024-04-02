class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursion(idx, currentSet):
            if idx == len(nums):
                results.append(currentSet)
                return
            
            #including the item at idx
            recursion(idx + 1, currentSet+[nums[idx]])
            
            #excluding the item at idx
            recursion(idx + 1, currentSet)
        
        results = []
        recursion(0,[])
        return results
