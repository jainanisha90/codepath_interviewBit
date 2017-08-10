import math
"""
Briefly take (n,k) = (4,21) for example, in the first iteration we divide the solution set into 4 groups: "1xxx", "2xxx", "3xxx", and "4xxx", while each group has 3! = 6 members.

From 21/6 = 3...3, we know that the 21th element is the 3rd element in the (3+1)th group. In this group, we can divide it into 3 sub-groups again: "41xx", "42xx" and "43xx", and each group has 2!=2 members.

Then, we calculate 3/2 and get 1...1, so it's the 1st element of (1+1)nd sub-group - "421x", and now it reach the base case with only one possibility - "4213".
"""
# Cantor ordering solution
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in xrange(1, n + 1)]
	print seq, k, fact, perm
        for i in reversed(xrange(n)):
            curr = perm[k / fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
            #print curr, seq, k, fact
        return seq

    def getPermutation1(self, n, k):
        array = range(1, n + 1)
        k = (k % math.factorial(n)) - 1
        permutation = []
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
	    #print idx, k
            permutation.append(array.pop(idx))
    
        return "".join(map(str, permutation))

    
if __name__ == "__main__":
    #print Solution().getPermutation(3, 2)
    print Solution().getPermutation1(4,21)	# Output 4213
