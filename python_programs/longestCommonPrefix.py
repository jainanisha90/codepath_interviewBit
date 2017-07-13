class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ""

        for i in range(len(A[0])):
            for string in A[1:]:
                if i >= len(string) or string[i] != A[0][i]:
                    return A[0][:i]
        return A[0]
        
print(Solution().longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"])
