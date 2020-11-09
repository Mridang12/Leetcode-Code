class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        NodeVisitList = list()
        for i in range(len(grid)):
            NodeVisitList.append([False]*len(grid[0]))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (not NodeVisitList[i][j]) and grid[i][j] == '1' :
                    islands += 1
                    self.DFS(grid, NodeVisitList, i, j)

        return islands

        
    def DFS(self, grid, NodeVisitList, row, col):        
        NodeVisitList[row][col] = True
        if (row > 0) :
            if (not NodeVisitList[(row-1)][col]) and grid[(row-1)][col] == '1':
                self.DFS(grid, NodeVisitList, (row-1), col)
        if (row < len(grid) - 1) : 
            if (not NodeVisitList[(row+1)][col]) and grid[(row+1)][col] == '1':
                self.DFS(grid, NodeVisitList, (row+1), col)
        if (col > 0) :
            if (not NodeVisitList[row][(col-1)]) and grid[row][(col-1)] == '1':
                self.DFS(grid, NodeVisitList, row, (col-1))
        if (col < len(grid[0])-1) :
            if (not NodeVisitList[row][(col+1)]) and grid[row][(col+1)] == '1':
                self.DFS(grid, NodeVisitList, row, (col+1))


        