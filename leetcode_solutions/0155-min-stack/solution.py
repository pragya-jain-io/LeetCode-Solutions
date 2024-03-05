class MinStack(object):

    def __init__(self):
        self.arr=list()
        self.length=0
        self.minimum=list()
        

    def push(self, val):
        if len(self.minimum)==0:
            self.minimum.append(val)
        else:
            if val<=self.minimum[-1]:
                self.minimum.append(val)
        self.length+=1
        self.arr.append(val)
        print("push",val,self.minimum)
        # else: 
        #     pass

    def pop(self):
        """
        :rtype: None
        """
        if self.length==0:
            pass
        else:
            popped=self.arr.pop()
            print("pop",self.minimum)
            if popped==self.minimum[-1]:

                self.minimum.pop()

            else:
                pass

    def top(self):
        """
        :rtype: int
        """
        if self.length==0:
            return []
        return self.arr[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
