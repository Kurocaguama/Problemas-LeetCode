class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        aux = []
        k = 0
        for i in nums:
            if i not in aux:
                aux.append(i)
                k +=1

        for i in range(len(aux)):
            nums[i] = aux[i]
        
        return k