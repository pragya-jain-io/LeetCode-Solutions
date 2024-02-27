class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key={"I":1,"V":5,"X":10,"C":100,"L":50,"D":500,"M":1000}
        num=0
        i=0
        while i< len(s):

            if i<(len(s)-1) and key[s[i]]<key[s[i+1]]:
                num+=(key[s[i+1]]-key[s[i]])
                i=i+2

            else:
                num+=key[s[i]]
                i+=1
        return num

        
