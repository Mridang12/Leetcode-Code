#Solution based on running DFS to find a back edge

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [0] * numCourses
        adj_list = list()
        for _ in range(numCourses):
            adj_list.append([])

        for i in range(len(prerequisites)):
            [u,v] = prerequisites[i]
            adj_list[u].append(v)
        
        noCycle = True

        for i in  range(numCourses) :
            if visited[i] == 0:
                noCycle = self.detectBackEdge(i, adj_list, visited)
            
            if not noCycle:
                break

        return noCycle

    #0 to denote not yet visited, -1 to denote visited in current DFS branch (to avoid cross-edge to be picked up as a back edge), 1 to denote permanently visited
    def detectBackEdge(self, u, adj_list, visited) :
        noCycle = True
        visited[u] = -1
        for v in adj_list[u]:
            if visited[v] == -1 :
                noCycle = False
                break
            elif visited[v] == 0 :
                noCycle = noCycle and self.detectBackEdge(v, adj_list, visited)
        
        visited[u] = 1
        return noCycle

    