class Solution:
    def reverse(self, x: int) -> int:
        n=0
        flag=0
        if x<0:
            x=x*-1
            flag=1
        while x>0:
            n=n*10+(x%10)
            x=x//10
        if n>2147483647:
            return 0
        if flag == 1:
            return n*-1
        return n
