class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]

        else:
            aux = self.getRow(rowIndex - 1)
            newRow = []
            for i in range(len(aux)):
                if i == 0:
                    newRow.append(aux[i])
                else:
                    newRow.append(aux[i-1] + aux[i])
            newRow.append(1)

        return newRow