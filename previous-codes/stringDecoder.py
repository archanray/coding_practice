class Solution():
	def dictInt(self):
		listOfInt = []
		for i in range(0,10):
			listOfInt.append(str(i))
		return listOfInt

	def recursiveStrDecoder(self, arr):
		output = ""
		n = len(arr)
		if n <= 1:
			return output
		intStack = []
		intList = self.dictInt()
		charStack = []
		flagInt = True
		for i in range(n):
			print(i, arr[i])
			if arr[i] in intList:
				if flagInt == True and i > 0:
					intStack[-1] = intStack[-1]*10+int(arr[i])
				else:
					intStack.append(int(arr[i]))
			else:
				flagInt = False
				if arr[i] != "]":
					charStack.append(arr[i])
				else:
					rep = intStack.pop()
					while charStack[-1] != "[":
						output = charStack.pop()+output
					charStack.pop()
					output = rep*output
		return output

inputs = "2[a2[b2[c]]]"
q = Solution()
print(q.recursiveStrDecoder(inputs))