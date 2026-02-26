class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []

        for i in range(n):
            if arr[i] != -1:
                L = max(0, i - arr[i])
                R = min(n - 1, i + arr[i])
                intervals.append((L, R))

        intervals.sort()

        curr = 0
        i = 0
        count = 0

        while curr < n:
            farthest = curr

            while i < len(intervals) and intervals[i][0] <= curr:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1

            if farthest == curr:
                return -1

            curr = farthest
            count += 1

        return count
