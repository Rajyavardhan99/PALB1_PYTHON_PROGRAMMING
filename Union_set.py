class Solution:    
    def findUnion(self, a, b):
        # code here
        union_set = set(a)
        union_set.update(b)
        
        return list(union_set)
