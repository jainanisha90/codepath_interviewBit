class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        n = int(A)
        if n < 2:
            return 0
        return 1 if n > 0 and (n & ~-n) == 0 else 0

print Solution().power(128) # Output 1
