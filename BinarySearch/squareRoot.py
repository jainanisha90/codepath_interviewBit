class Solution:
    def sqrt(self, A):
        l, r = 0, A
        while l <= r:
            mid = (l + r)//2
	    #print mid
            if mid*mid <= A < (mid+1) * (mid+1):
                return mid
            elif mid * mid > A:
                r = mid
            else:
                l = mid + 1

print Solution().sqrt(4) # Output 2
print Solution().sqrt(2) # Output 1 
print Solution().sqrt(0) # Output 0 
