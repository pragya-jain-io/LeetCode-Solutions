class MyStack(object):

    def __init__(self):
        self.array=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # logic : add an element to a q2, shift all the elements from q1 to q2, swap q1 and q2
        self.array=[x,]+self.array

        

    def pop(self):
        """
        :rtype: int
        """
        ans=self.array[0]
        self.array=self.array[1:]
        return ans
        

    def top(self):
        """
        :rtype: int
        """
        return self.array[0]

    def empty(self):
        """
        :rtype: bool
        """
        return True if self.array==[] else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
