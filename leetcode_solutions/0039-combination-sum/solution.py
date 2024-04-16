class Solution(object):
    def combinationSum(self, c, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def generate(index,arr,target):

            if target <=0 or index>=len(c):
                if target==0:
                    ans.append(arr)
                return
            
            generate(index,arr+[c[index],],target-c[index])
            generate(index+1,arr,target)

        ans=[]
        generate(0,[],t)
        return ans
        
