class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        dist = {}
        for i in range(n):
            adj[i] = []
            dist[i] = float('inf')
        dist[src] = 0
        
        for s, d, w in edges:
            adj[s].append([d,w])
        
        heap = [(0, src)]

        while heap:
            curr_dist, curr = heapq.heappop(heap)
            for d,w in adj[curr]:
                if curr_dist + w < dist[d]:
                    dist[d] = curr_dist + w
                    heapq.heappush(heap, (dist[d], d))
        
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
            
        return dist
     