class Solution:
    def relativeSortArray(self, arr1, arr2):
        """
        stupid solution is the best solution lol
        """
        sorted_list = []
        for x in arr2:
            while x in arr1:
                sorted_list.append(x)
                arr1.remove(x)
        if len(arr1) != 0:
            arr1 = sorted(arr1)
        sorted_list = sorted_list+arr1
        
        return sorted_list

input1 = [28,6,22,8,44,17]
input2 = [22,28,8,6]
print(Solution().relativeSortArray(input1, input2))