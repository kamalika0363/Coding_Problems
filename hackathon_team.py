def countTeams(teamSize_1, teamSize_2, p):
    def can_divide(x):
        return (p - x * teamSize_1) % teamSize_2 == 0 and (p - x * teamSize_1) >= 0

    for i in range(p // teamSize_1 + 1):
        if can_divide(i):
            return i + (p - i * teamSize_1) // teamSize_2

    return -1


# Test the function
print(countTeams(3, 4, 7))  # Expected output: 2
print(countTeams(3, 4, 6))  # Expected output: 2
