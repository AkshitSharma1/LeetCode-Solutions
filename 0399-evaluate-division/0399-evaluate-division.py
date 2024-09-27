from collections import defaultdict

class Solution:
    def dfs(self, curr_node, target_node, visited, adj_list, value):
        if curr_node == target_node:
            return value
        
        visited.add(curr_node)
        for neighbor, weight in adj_list[curr_node]:
            if neighbor not in visited:
                result = self.dfs(neighbor, target_node, visited, adj_list, value * weight)
                if result != -1:
                    return result
        return -1

    def calcEquation(self, equations, values, queries):
        adj_list = defaultdict(list)

        # Build adjacency list
        for (dividend, divisor), value in zip(equations, values):
            adj_list[dividend].append((divisor, value))
            adj_list[divisor].append((dividend, 1 / value))

        # Process queries
        answer = []
        for dividend, divisor in queries:
            if dividend not in adj_list or divisor not in adj_list:
                answer.append(-1.0)
            elif dividend == divisor:
                answer.append(1.0)
            else:
                visited = set()
                answer.append(self.dfs(dividend, divisor, visited, adj_list, 1.0))

        return answer
