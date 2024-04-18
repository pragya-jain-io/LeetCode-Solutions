class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def generate(sr,arr):
            if sr == "":
                print(arr)
                ans.append(arr)
                return
            for i in range(1,len(sr)+1):
                ss=sr[0:i]
                if sr[0:i]==ss[::-1]:
                    print("ss", sr[i:], arr+[ss,])
                    generate(sr[i:], arr+[ss,])
                else:
                    pass


        ans=[]
        generate(s,[])
        return ans


# print(partition("aab"))


        
