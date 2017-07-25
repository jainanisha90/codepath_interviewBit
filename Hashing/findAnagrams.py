class Solution:
    def findAnagrams(self, word):
        result = []
	count = {}
	sum = 0
	length = len(word)
	for i in range(26):
	    count[i] = 0
	
	if length % 2 == 1:
	    return -1

	else:
	    for i in range(int(length/2)):
		count[ord(word[i]) - ord('a')] += 1
		
	    for i in range(length/2, length):
		count[ord(word[i]) - ord('a')] -= 1

	    for i in range(26):
		sum += self.mod(count[i])
	    sum = sum/2

	return sum

    def mod(self, x):
	if x<0:
	    return -1 * x
	else:
	    return x



if __name__ == "__main__":
    obj = Solution()
    print obj.findAnagrams('dnqaurlplofnrtmh') # Output 5
    li = ['aaabbb', 'ab', 'abc', 'mnop', 'xyyx']
    for string in li:
	print obj.findAnagrams(string)	# 3 1 -1 2 0
    """
    print obj.findAnagrams(1, ['hhpddlnnsjfoyxpciioigvjqzfbpllssuj'])
    print obj.findAnagrams(1, ['xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj'])
    print obj.findAnagrams(1, ['dnqaurlplofnrtmh'])
    print obj.findAnagrams(1, ['aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb'])
    print obj.findAnagrams(1, ['lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad'])
    print obj.findAnagrams(1, ['drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe'])
    print obj.findAnagrams(1, ['ubulzt'])
    print obj.findAnagrams(1, ['vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy'])
    print obj.findAnagrams(1, ['xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa'])
    print obj.findAnagrams(1, ['gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv'])
    """
