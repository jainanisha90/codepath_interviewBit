class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        A, B = A[::-1], B[::-1]
        result = [0] * (len(A) + len(B))
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                result[i + j] += int(A[i]) * int(B[j])
                result[i + j + 1] += result[i + j] / 10
                result[i + j] %= 10
        result = result[::-1]
        return ''.join([str(i) for i in result]).lstrip('0') or '0'
       
print Solution().multiply("12", "10") # Output "120"
