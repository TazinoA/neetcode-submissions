class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        explored = set()
        unexplored = set()
        curr_min = float('inf')
        curr_edges = []
        curr = src
        dist = {
            src:0
        }
        explored.add(src)

        for i in range(n):
            if i not in unexplored and i != src:
                unexplored.add(i)
                dist[i] = float('inf')
        
        while unexplored:
            for edge in edges:
                if edge[0] == curr:
                    curr_edges.append(edge)
            for edge in curr_edges:
                val = edge[2] + dist[curr]
                if val < dist[edge[1]]:
                    dist[edge[1]] = val
            for vertex in unexplored:
                if dist[vertex] <= curr_min:
                    curr_min = dist[vertex]
                    curr = vertex
            unexplored.remove(curr)
            explored.add(curr)
            curr_edges = []
            curr_min = float('inf')
                 
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist