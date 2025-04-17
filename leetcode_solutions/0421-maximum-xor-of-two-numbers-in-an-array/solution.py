class Trie:

    def __init__(self, n = 32):
        self.bit = [None,None]
        self.n = n

    def insert(self, number):
        number = format(number, '032b')
        node = self
        for i in number:
            if not node.bit[int(i)]:
                node.bit[int(i)] = Trie(n = node.n - 1)
            node = node.bit[int(i)]

    def max_xor(self, number):
        number = format(number, '032b')
        node = self
        answer = 0
        for i in number:
            if i == "0" and node.bit[1]:
                node = node.bit[1]
                answer += 2**(node.n)
            elif i=="1" and node.bit[0]:
                node = node.bit[0]
                answer += 2**(node.n)
            else:
                node = node.bit[0] or node.bit[1]
        return answer
                


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()
        for i in nums:
            t.insert(i)

        max_answer = 0
        
        for i in nums:
            ans = t.max_xor(i)
            if ans>max_answer:
                max_answer = ans
            else:
                pass
        
        return max_answer
        
