class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        # Edge cases
        if m == 0 or n == 0:
            return 0
        if m > n:
            return -1
        
        # Step 1: sort
        arr.sort()
        
        # Step 2: sliding window
        min_diff = float('inf')
        
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
