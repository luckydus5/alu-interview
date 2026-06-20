#!/usr/bin/python3
"""Module that computes how much rainwater is retained between walls."""


def rain(walls):
    """Calculate the total amount of rainwater retained between walls.

    Given a list of non-negative integers representing the heights of
    walls of unit width 1, return the number of square units of water
    retained after it rains. The two ends of the list never retain
    water.

    Args:
        walls (list): A list of non-negative integers.

    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]

    return water
