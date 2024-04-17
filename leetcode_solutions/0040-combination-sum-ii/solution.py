class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(candidates)
        candidates.sort()
        def generate(index,arr,diff):
            if index>=n or diff<=0:
                if diff==0:
                    print(arr)
                    ans.append(arr)
                return
            le=candidates[index]
            generate(index+1,arr+[le,],diff-le)
            for i in range(index,n):
                if le==candidates[i]:
                    continue
                else:
                    le=candidates[i]
                    generate(i+1,arr+[candidates[i],],diff-candidates[i])
            

        ans=[]
        generate(0,[],target)
        return ans
            
        
