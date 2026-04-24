class Solution:
    def countPairs(self, arr):
        from collections import defaultdict
        
        n = len(arr)
        m = len(arr[0])
        ans = 0
        
        for i in range(m):
            freq = defaultdict(int)
            
            for s in arr:
                # remove i-th character
                key = s[:i] + s[i+1:]
                freq[key] += 1
            
            # count pairs
            for count in freq.values():
                if count > 1:
                    ans += count * (count - 1) // 2
        
        return ans
