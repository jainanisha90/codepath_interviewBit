class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if B == A[mid]:
                return mid
            if A[left] == A[mid] and A[mid] == A[right]:
                left += 1
                right -= 1
            elif A[left] <= A[mid]:
                if A[left]<=B<A[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if A[mid]<B<=A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == "__main__":
    print Solution().search([3, 5, 1], 3)	# Output 0
    print Solution().search([2, 2, 3, 3, 4, 1], 1)	# Output 5
    print Solution().search([4, 4, 5, 6, 7, 0, 1, 2], 5)	# Output 2
