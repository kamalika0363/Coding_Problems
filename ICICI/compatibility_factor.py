"""
A school is organizing a picnic for all its students. There is a total of N
students labeled from 1 to N in the school. Each student left has a
compatibility factor of Xi.
It is time for the picnic and all students to stand in a line. The student line
is to be split into groups. A set of consecutive students standing in a line
can form a group. For the picnic to be safe, each group must have at least
2 students with the same compatibility factor.
Finding the maximum number of groups that can be created.
"""
from typing import List


def max_groups(N: int, X: List[int]):
    groups = 0
    left = 0

    while left < N:
        right = left + 1
        while right < N and X[right] != X[left]:
            right += 1
        if right < N:
            groups += 1
            left = right + 1
        else:
            left += 1
    return groups


N = 8
X = [1, 2, 1, 1, 1, 1, 1, 1]
print(max_groups(N, X))
