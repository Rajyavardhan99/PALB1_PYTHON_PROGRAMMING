class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If array has only one element
        if n <= 1:
            return 0
        
        # If first element is 0 → cannot move
        if arr[0] == 0:
            return -1
        
        maxReach = arr[0]   # farthest we can reach
        steps = arr[0]      # steps we can still take
        jumps = 1           # at least one jump needed
        
        for i in range(1, n):
            
            # If we reached last index
            if i == n - 1:
                return jumps
            
            # Update maxReach
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step
            steps -= 1
            
            # If no steps left
            if steps == 0:
                jumps += 1
                
                # If current index is beyond maxReach → can't move
                if i >= maxReach:
                    return -1
                
                # Reinitialize steps
                steps = maxReach - i
        
        return -1
