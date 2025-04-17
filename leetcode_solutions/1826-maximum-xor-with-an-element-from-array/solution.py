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
    def sortQuery(self, queries, key_index=1):
        return sorted(
            [(q[0], q[1], i) for i, q in enumerate(queries)],
            key=lambda x: x[key_index]
        )

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sortedQueries = self.sortQuery(queries)
        nums.sort()
        pointer = 0
        t=Trie()
        answer = [None]*len(queries)
        for i in sortedQueries:
            print(i)
            while pointer<len(nums) and nums[pointer]<=i[1]:
                t.insert(nums[pointer])
                pointer+=1
            if pointer == 0:
                answer[i[2]]=-1
            else:
                answer[i[2]]=t.max_xor(i[0])
        return answer
        
            


