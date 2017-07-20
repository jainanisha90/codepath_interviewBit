class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = [str(x) for x in A]
        A.sort(cmp=lambda x, y: cmp(y + x, x + y))
        largest = ''.join(A)
        return largest.lstrip('0') or '0'

print Solution().largestNumber([3, 30, 34, 5, 9]) # Output 9534330
