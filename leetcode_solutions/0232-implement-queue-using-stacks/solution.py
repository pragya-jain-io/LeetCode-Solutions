class MyQueue(object):

    def __init__(self):
        self.array=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # logic - s1 to s2, add element to s1, add s2 back to s1
        self.array=[x,]+self.array


        

    def pop(self):
        """
        :rtype: int
        """
        ans=self.array[-1]
        self.array=self.array[:len(self.array)-1]
        return ans
        

    def peek(self):
        """
        :rtype: int
        """
        return self.array[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return True if self.array==[] else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
