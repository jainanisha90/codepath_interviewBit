class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        result = 0
        while A:
            A &= A - 1
            result += 1
        return result

print Solution().numSetBits(11)	# Output 3
