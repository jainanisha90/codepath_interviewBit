class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        dic = {}
        for i in range(len(A)):
            temp = ''.join(sorted(A[i]))
            if temp in dic:
                dic.get(temp).append( i + 1 )
            else:
                dic[temp] = [i + 1]
        return dic.values()

print Solution().anagrams(['cat', 'dog', 'god', 'tca']) # Output [[1, 4], [2, 3]]
