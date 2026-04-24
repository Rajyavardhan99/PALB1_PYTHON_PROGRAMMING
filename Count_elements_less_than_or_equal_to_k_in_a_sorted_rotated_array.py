class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        
        # Find pivot (smallest element index)
        def findPivot():
            low, high = 0, n - 1
            while low < high:
                mid = (low + high) // 2
                if arr[mid] > arr[high]:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        pivot = findPivot()
        
        # Count elements ≤ x in sorted subarray
        def count(l, r):
            left, right = l, r
            ans = l - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= x:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans - l + 1
        
        return count(0, pivot - 1) + count(pivot, n - 1)
