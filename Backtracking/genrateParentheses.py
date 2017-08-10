class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        def genParenthesisRecurr(result, paren, left, right):
            if left == 0 and right == 0:
                result.append(paren)
            if left > 0:
                genParenthesisRecurr(result, paren + "(", left-1, right)
            if left < right:
                genParenthesisRecurr(result, paren + ")", left, right-1)
        
        result = []
        genParenthesisRecurr(result, "", A, A)
        return result
        

print Solution().generateParenthesis(3)	# Output ['((()))', '(()())', '(())()', '()(())', '()()()']
