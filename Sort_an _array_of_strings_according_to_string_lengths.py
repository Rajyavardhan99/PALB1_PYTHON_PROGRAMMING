class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)   # sort in-place
        return arr
