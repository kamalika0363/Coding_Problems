"""
A set of computers need to be connected using ethernet cables. Two computers are said to be connected if they have
either a direct or indirect connection to each other via cables. An example of a direct connection would be a cable
connecting computers 1 an 2. If computer 2 were then directly connected to computer 3, we would say that computers 1
and 3 are indirectly connected. A cable only connects two distinct computers. No two computers are connected by more
than one cable.
Initially, some groups of computers are connected to each other. If some groups of computers are
disconnected, one operation may be performed: remove the cable between any two computers and connect any other pair
of computers with the cable. Determine the minimum number of operations to connect all the computers. Report -1 as
the answer if it is not possible to connect all the computers.
"""
from collections import defaultdict


class NetworkConnectionOptimizer:
    def __init__(self, n):
        self.n = n  # number of computers
        self.graph = defaultdict(list)
        self.visited = [False] * (n + 1)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v):
        self.visited[v] = True
        for neighbor in self.graph[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)

    def count_components(self):
        self.visited = [False] * (self.n + 1)
        components = 0
        for i in range(1, self.n + 1):
            if not self.visited[i]:
                self.dfs(i)
                components += 1
        return components

    def min_operations(self, c_from, c_to):
        total_cables = len(c_from)

        # Add all connections to the graph
        for u, v in zip(c_from, c_to):
            self.add_edge(u, v)

        # Count the number of connected components
        components = self.count_components()

        # Calculate the minimum number of operations needed
        min_ops = components - 1

        # Check if it's possible to connect all computers
        if total_cables < self.n - 1 or min_ops > total_cables:
            return -1

        return min_ops


# Example usage:
comp_nodes = 4  # number of computers
comp_edges = 3  # number of edges
c_from = [1, 1, 2]
c_to = [2, 3, 3]

optimizer = NetworkConnectionOptimizer(comp_nodes)
result = optimizer.min_operations(c_from, c_to)
print(f"Minimum number of operations: {result}")