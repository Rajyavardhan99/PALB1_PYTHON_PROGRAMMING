import heapq

class Solution:
    def minOperations(self, arr):
        total_sum = sum(arr)
        target = total_sum / 2

        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)

        curr_sum = total_sum
        operations = 0

        while curr_sum > target:
            largest = -heapq.heappop(max_heap)
            half = largest / 2
            curr_sum -= half
            heapq.heappush(max_heap, -half)
            operations += 1

        return operations
