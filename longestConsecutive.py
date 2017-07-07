class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        result, lengths = 1, {key: 0 for key in A}
        for i in A:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
                length = 1 + left + right
                result, lengths[i - left], lengths[i + right] = max(result, length), length, length
        return result
