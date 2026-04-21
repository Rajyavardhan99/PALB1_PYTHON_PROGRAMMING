class Solution:
    def spirallyTraverse(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        result = []
        
        while top <= bottom and left <= right:
            
            # 1. Left → Right
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            # 2. Top → Bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # 3. Right → Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            # 4. Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result
