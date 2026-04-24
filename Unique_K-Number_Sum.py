class Solution:
    def combinationSum(self, n, k):   # <-- FIXED ORDER
        res = []
        
        def backtrack(start, path, total):
            if len(path) == k and total == n:
                res.append(path[:])
                return
            
            if len(path) > k or total > n:
                return
            
            for num in range(start, 10):
                if total + num > n:   # pruning
                    break
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()
        
        backtrack(1, [], 0)
        return res
