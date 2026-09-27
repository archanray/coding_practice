class Solution:
    def letterPatches(self, digit: str) -> str:
        dictOfAssociation = {
                            "2": ["a", "b", "c"],
                            "3": ["d", "e", "f"],
                            "4": ["g", "h", "i"],
                            "5": ["j", "k", "l"],
                            "6": ["m", "n", "o"],
                            "7": ["p", "q", "r", "s"],
                            "8": ["t", "u", "v"],
                            "9": ["w", "x", "y", "z"]
                            }
        if digit in dictOfAssociation.keys():
            return dictOfAssociation[digit]
        else:
            return []
    def outerProduct(self, list1, list2):
        if list1 == []:
            return list2
        else:
            listout = [x+y for x in list1 for y in list2]
        return listout
    def letterCombinations(self, digits: str) -> list[str]:
        list1 = []
        for i, a in enumerate(digits):
            list2 = self.letterPatches(a)
            list1 = self.outerProduct(list1, list2)
        return list1

q = Solution()

print(q.letterCombinations("2"))