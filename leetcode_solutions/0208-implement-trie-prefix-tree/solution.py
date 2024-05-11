class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current =node

        current.end=True
        print("success") 
        # t - o(m) s- o(m)


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.end==True:
            return True
        else:
            return False



    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        currentNode = self.root
        for i in prefix:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
