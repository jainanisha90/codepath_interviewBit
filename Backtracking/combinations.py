class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        result = []
        self.combineRecu(n, result, 0, [], k)
        return result
    
    def combineRecu(self, n, result, start, intermediate, k):
        if k == 0:
            result.append(intermediate[:])
        for i in xrange(start, n):
            intermediate.append(i + 1)
            self.combineRecu(n, result, i + 1, intermediate, k - 1)
            intermediate.pop()

print Solution().combine(4, 3)	# Output [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]