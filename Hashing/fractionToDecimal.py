class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
	"""
        result = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            reuslt = "-"
        
        dividend, divisor = abs(numerator), abs(denominator)
        result += str(dividend / divisor)
        dividend %= divisor
        
        
        if dividend > 0:
            result += "."
            
        lookup = {}
        while dividend and dividend not in lookup:
            lookup[dividend] = len(result)
            dividend *= 10
            result += str(dividend / divisor)
            dividend %= divisor
            
        if dividend in lookup:
            result = result[:lookup[dividend]] + "(" + result[lookup[dividend]:] + ")"

        return result
        

if __name__ == "__main__":
    print Solution().fractionToDecimal(1, 9)	# 0.(1)
    print Solution().fractionToDecimal(-50, 8) 	# 6.25
    print Solution().fractionToDecimal(22, 2)	# 11
    print Solution().fractionToDecimal(-22, -2)	# 11
