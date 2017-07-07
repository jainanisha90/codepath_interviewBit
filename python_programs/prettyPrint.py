class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = 2*A -1
        array = [[0 for x in xrange(size)] for y in xrange(size)]
        for i in xrange(0,size):
            for j in xrange(i, size-i):
                array[i][j] = A -i
                array[j][i] = A -i
                array[size-1-i][j]=A-i
                array[j][size-1-i]=A -i 
        return array
