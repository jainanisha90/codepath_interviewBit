class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        for i in range(len(A)):
                for j in range(i, len(A)):
                        if A[j] > A[i]:
                                A[i] = A[j]
                                break
                else:
                        A[i] = -1

        return(A)

print Solution().nextGreater([4, 5, 2, 10]) #Output : [5, 10, 10, -1]
