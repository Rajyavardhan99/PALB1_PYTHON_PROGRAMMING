class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        
        if n == 1:
            return 0
        
        arr.sort()
        
        ans = arr[n - 1] - arr[0]
        
        for i in range(n - 1):
            min_height = min(arr[0] + k, arr[i + 1] - k)
            max_height = max(arr[n - 1] - k, arr[i] + k)
            
            if min_height < 0:
                continue
            
            ans = min(ans, max_height - min_height)
        
        return ans
