class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        
        for i in range(numRows-1):
            pascal[i].append(0)
            pascal[i].insert(0,0)

            new_row = [pascal[i][j]+pascal[i][j+1] for j in range(len(pascal[i])-1)]
            
            pascal[i].pop()
            pascal[i].remove(0)

            pascal.append(new_row)
        return pascal