ass Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        result = []
        used = [False] * len(A)
        self.permuteRecurr(result, used, [], A)
        return result
        
    def permuteRecurr(self, result, used, inter, A):
        if len(inter) == len(A):
            result.append(inter + [])
            return
        for i in range(len(A)):
            if not used[i]:
                used[i] = True
                inter.append(A[i])
                self.permuteRecurr(result, used, inter, A)
                inter.pop()
                used[i] = False

if __name__ == "__main__":
    print Solution().permute([1, 2, 3])	# Output [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
