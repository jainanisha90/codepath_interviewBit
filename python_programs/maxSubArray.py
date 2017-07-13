class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if max(A) < 0:
            return max(A)
        max_sub_array, non_continous_max = float("-inf"), 0
        for num in A:
            non_continous_max = max(0, non_continous_max + num)
            max_sub_array = max(max_sub_array, non_continous_max)
        return max_sub_array
        
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
