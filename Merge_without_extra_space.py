class Solution:
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        
        def nextGap(gap):
            if gap <= 1:
                return 0
            return (gap // 2) + (gap % 2)
        
        gap = nextGap(n + m)
        
        while gap > 0:
            i = 0
            while i + gap < n + m:
                
                # Both elements in array a
                if i < n and i + gap < n:
                    if a[i] > a[i + gap]:
                        a[i], a[i + gap] = a[i + gap], a[i]
                
                # One element in a, one in b
                elif i < n and i + gap >= n:
                    if a[i] > b[i + gap - n]:
                        a[i], b[i + gap - n] = b[i + gap - n], a[i]
                
                # Both elements in array b
                else:
                    if b[i - n] > b[i + gap - n]:
                        b[i - n], b[i + gap - n] = b[i + gap - n], b[i - n]
                
                i += 1
            
            gap = nextGap(gap)
