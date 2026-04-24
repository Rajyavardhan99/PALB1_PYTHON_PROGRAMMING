class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        left = [0] * n
        stack = []
        
        # LEFT SIDE
        for i in range(n):
            count = 0
            while stack and stack[-1][0] < arr[i]:
                count += stack[-1][1] + 1
                stack.pop()
            
            left[i] = count
            stack.append((arr[i], count))
        
        # RIGHT SIDE
        right = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1][0] < arr[i]:
                count += stack[-1][1] + 1
                stack.pop()
            
            right[i] = count
            stack.append((arr[i], count))
        
        # RESULT
        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] + 1)
        
        return ans
