class Solution:
    def prevSmaller(self, arr):
        stack = []
        result = []
        
        for num in arr:
            # Pop until we find smaller element
            while stack and stack[-1] >= num:
                stack.pop()
            
            # If stack is empty → no smaller element
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            stack.append(num)
        
        return result
