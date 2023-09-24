class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while j!=i and (j<len(s) and i<len(s)):
            if (s[i].isalnum() and s[j].isalnum()):
                if s[j].lower()==s[i].lower():
                    j=j-1
                    i=i+1
                else:
                    return False
            else:
                if not s[i].isalnum():
                    i+=1
                elif not s[j].isalnum(): 
                    j=j-1
        return True
        
