class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for num in A:
            res ^= num
        return res

print Solution().singleNumber([1 2 2 3 1])	# Output 3
