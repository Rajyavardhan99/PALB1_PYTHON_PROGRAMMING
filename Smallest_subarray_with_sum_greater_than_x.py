class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        
        left = 0
        curr_sum = 0
        min_len = n + 1
        
        for right in range(n):
            curr_sum += arr[right]
            
            # IMPORTANT CHANGE: >= instead of >
            while curr_sum >= x:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1
        
        return min_len if min_len != n + 1 else 0
