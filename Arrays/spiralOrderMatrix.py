class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        left, right, top, bottom , num= 0, A-1, 0, A-1, 1
        matrix = [[0 for _ in range(A)] for _ in range(A)]
        
        while left <= right and top <= bottom:
            for i in xrange(left, right+1):
                matrix[top][i] = num
                num += 1
            for j in xrange(top+1, bottom):
                matrix[j][right] = num
                num += 1
            for i in reversed(xrange(left, right+1)):
                if top < bottom:
                    matrix[bottom][i] = num
                    num +=1
            for j in reversed(xrange(top+1, bottom)):
                if left < right:
                    matrix[j][left] = num
                    num += 1
            
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    
        return matrix
           
print Solution().generateMatrix(3) # Output [[ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ]] 
