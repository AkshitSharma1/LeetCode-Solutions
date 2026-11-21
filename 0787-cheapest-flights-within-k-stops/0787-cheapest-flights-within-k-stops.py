class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        min_dist = [float("inf")]*n
        adj_list = defaultdict(list)
        for flight in flights:
            fro,to,price = flight
            adj_list[fro].append(to)

        min_dist[src] = 0
        for _ in range(k+1):
            temp = min_dist.copy()
            for flight in flights:
                fro,to,price = flight
                temp[to] = min(temp[to],min_dist[fro]+price)
            min_dist = temp.copy()
        return min_dist[dst] if min_dist[dst]!=float("inf") else -1
