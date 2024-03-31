class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod= 1000000007
        odd= (n//2)
        even=(n//2)+(n % 2)

        def power(x,np):
            if np==0:
                return 1
            else:
                if np%2:
                    return (x * power( x , np - 1 )) % mod
                else:
                    return ( power ( ( ( x * x ) % mod) , np // 2))
        return ( ( power(4,odd))*power(5,even))%mod
            
        # mod = 10 ** 9 + 7
        # odd = (n // 2)
        # even = (n // 2) + n % 2

        # def power(x, np):
        #     if np == 0:
        #         return 1
        #     if np % 2:
        #         return (x * power(x, np - 1)) % mod
        #     return power((x * x) % mod, (np // 2))

        # return (power(4, odd) * power(5, even)) % mod
        
