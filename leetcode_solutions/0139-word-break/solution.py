class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
    
        def traverse(word, dictionary, flag):
            if word == "":
                flag = True
                return flag
            if word in memo:
                return memo[word]
            for i in range(1, len(word) + 1):
                if word[:i] in dictionary:
                    flag = traverse(word[i:], dictionary, flag)
                    if flag:
                        memo[word] = True
                        return True
            memo[word] = False
            return flag
        
        return traverse(s, wordDict, False)

