"""
A=3  
          00000000000000000000000000000011 
=>        11000000000000000000000000000000
"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result = 0
        for i in xrange(32):
            result <<= 1
            result |= A & 1
            A >>= 1
        return result

print Solution().reverse(3)	# Output 3221225472
