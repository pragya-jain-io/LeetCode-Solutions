class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=list()
        for i in s:
            if i in "({[":
                stack.append(i)
            if i in ")}]":
                if len(stack)==0:
                    return False
                if i==")":
                    # if len(stack)==0:
                    #     print(1)
                    #     return False
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        stack.append(i)
                    # elif len(stack)!=0:
                    #     print(2)
                    #     return False
                elif i=="]":
                    # if len(stack)==0:
                    #     print(3)
                    #     return False
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        stack.append(i)
                    # elif len(stack)!=0:
                    #     print(4)
                    #     return False
                elif i=="}":
                    # if len(stack)==0:
                    #     print(5)
                    #     return False
                    if stack[-1]=="{":
                        stack.pop()
                    else:
                        stack.append(i)
                    # if len(stack)!=0:
                    #     print(6)
                    #     return False
        if len(stack)==0:
            return True 
        else:
            return False    
                    
                    
