"""A list of ranges contains the start and end values continuous ranges of integers. For example, [1, 4] denotes all
integers in the range 1 to 4, or [1, 2, 3, 4].
Divide the ranges into 2 groups such that any 2 ranges that have at least one common integer belong to the same group.
Given the list of ranges, find the number of ways to distribute these ranges into 2 groups that satisfy the constraint
and each group has at least one range.
Since the answer can be large, compute it modulo (10^9+7).
Example Consider ranges = [[1, 5], [3, 8], [10, 15], [13, 14], [20, 100]].
"""
from collections import defaultdict


class RangeGroupingCalculator:
    def __init__(self):
        self.MOD = 10 ** 9 + 7

    def count_groupings(self, ranges):
        # Sort ranges by start time
        ranges.sort()

        # Build graph of overlapping ranges
        graph = defaultdict(list)
        for i in range(len(ranges)):
            for j in range(i + 1, len(ranges)):
                if ranges[i][1] >= ranges[j][0]:  # Ranges overlap
                    graph[i].append(j)
                    graph[j].append(i)
                else:
                    break  # No need to check further as ranges are sorted

        # Count connected components
        visited = [False] * len(ranges)
        components = []

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        for i in range(len(ranges)):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(component)

        # Calculate the number of ways to distribute
        if len(components) == 1:
            return 0  # Can't divide into two non-empty groups
        elif len(components) == 2:
            return 1  # Only one way to divide
        else:
            # Use 2^(n-1) - 1 formula
            return (pow(2, len(components) - 1, self.MOD) - 1) % self.MOD


# Example usage
calculator = RangeGroupingCalculator()
ranges = [[1, 5], [3, 8], [10, 15], [13, 14], [20, 100]]
result = calculator.count_groupings(ranges)
print(f"Number of ways to distribute ranges: {result}")