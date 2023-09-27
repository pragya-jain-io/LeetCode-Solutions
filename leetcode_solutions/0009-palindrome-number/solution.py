class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=0
        temp=x
        while x>0:
            n=(n*10)+(x%10)
            x=x//10
        if temp!=n:
            return False 
        return True
