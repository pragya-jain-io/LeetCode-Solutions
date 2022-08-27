class Solution:
    def romanToInt(self, s: str) :
        dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        summ=0
        for i in range (len(s)):
            if i<(len(s)-1) and dictionary[s[i]]<dictionary[s[i+1]] :
                summ+=(-1*dictionary[s[i]])
            else:
                summ+=dictionary[s[i]]
                
        return summ
