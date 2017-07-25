class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(A):
            if visited[ord(char)]:
                while char != A[start]:
                    visited[ord(A[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

if __name__ == "__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")	# Output 3
