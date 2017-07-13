class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        num = A[0]
        other_num = A[A[0]]
        while num != other_num:
            num = A[num]
            other_num = A[A[other_num]]

        other_num = 0
        while num != other_num:
            num = A[num]
            other_num = A[other_num]
        return num
       
print(Solution().repeatedNumber([3 4 1 4 1])
