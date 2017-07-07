class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        count = 0
        end = len(A)-1
        tot = 0
        temp_sum = 0
        temp_array = []
        tot_sum = sum(A[0:len(A)])
        for i in range(len(A)):
            current_sum = 0
            for j in range(i,len(A)):
                current_sum += A[j]
                if(current_sum > C):
                    break
                elif(B <= current_sum <= C):
                    #print current_sum
                    tot += 1
            tot_sum -= A[i]
            if(tot_sum < B):
                break
        return tot
