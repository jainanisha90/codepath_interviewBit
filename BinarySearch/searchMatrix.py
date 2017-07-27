class Solution:
	def searchMatrix(self, matrix, target):
		r, c = 0, len(matrix[0])-1
		while r <= c:
			if matrix[r][c] == target:
				return True
			elif matrix[r][c] < target:
				r = r+1
			elif matrix[r][c] > target:
				c = c-1
		return False

matrix = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
print Solution().searchMatrix(matrix, 12)
print Solution().searchMatrix(matrix, 20)
