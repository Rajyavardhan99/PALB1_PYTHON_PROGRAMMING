class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: count good elements
        good = sum(1 for x in arr if x <= k)
        
        # Step 2: count bad elements in first window
        bad = sum(1 for x in arr[:good] if x > k)
        
        ans = bad
        
        # Step 3: sliding window
        i = 0
        j = good
        
        while j < n:
            # element going out
            if arr[i] > k:
                bad -= 1
            
            # element coming in
            if arr[j] > k:
                bad += 1
            
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans
