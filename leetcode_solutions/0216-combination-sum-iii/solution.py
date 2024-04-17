class Solution(object):
    def combinationSum3(self, k, n):
        ans=[]
        # digits=[1,2,3,4,5,6,7,8,9]
    
        def generate(index,arr,sum):
            print("array->",arr)
            if index>=9 or len(arr)>=k or sum>=n:
                if len(arr)==k and sum==n:
                    print(arr,sum)
                    ans.append(arr)
                return
            generate(index+1, arr+[index+1,], sum+index+1)
            generate(index+1,arr,sum)
        
        generate(0,[],0)
        return ans
