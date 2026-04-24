class Solution:
    def frequencySort(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        result = []
        for ch, count in chars:
            result.append(ch * count)
        
        return "".join(result)
