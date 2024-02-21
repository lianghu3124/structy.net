import unittest

"""
--- Count paths ---
Write a function, count_paths, that takes in a grid as an argument. In the grid, 'X' represents walls and 'O' represents open spaces. You may only move down or to the right and cannot pass through walls. The function should return the number of ways possible to travel from the top-left corner of the grid to the bottom-right corner.
"""

# this is better than  count_paths
def count_paths2(grid):
    return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
    pos = (r,c)

    if pos in memo:
        return memo[pos]
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'X':
        return 0
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    
    down_paths = _count_paths(grid, r+1, c, memo)
    right_paths = _count_paths(grid, r, c+1, memo)

    memo[pos] = down_paths + right_paths 

    return memo[pos]

"""
r = # rows
c = # columns
Time: O(r*c)
Space: O(r*c)

"""

def count_paths(grid):
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    return calculate((0, 0), (rows, cols), grid, {})


def calculate(start, end, grid, memo):

    if start in memo:
        return memo[start]
    if start == end:
        return 1

    row, col = start
    next_row = row + 1
    next_col = col + 1
    max_row, max_col = end

    result = 0

    # down
    if next_row <= max_row and grid[next_row][col] == "O":
        result += calculate((next_row, col), end, grid, memo)
    # right
    if next_col <= max_col and grid[row][next_col] == "O":
        result += calculate((row, next_col), end, grid, memo)

    memo[start] = result
    return result


class Test(unittest.TestCase):

    def test_00(self):
        grid = [
            ["O", "O"],
            ["O", "O"],
        ]
        assert count_paths(grid) == 2

    def test_01(self):
        grid = [
            ["O", "O", "X"],
            ["O", "O", "O"],
            ["O", "O", "O"],
        ]
        assert count_paths(grid) == 5

    def test_02(self):
        grid = [
            ["O", "O", "O"],
            ["O", "O", "X"],
            ["O", "O", "O"],
        ]
        assert count_paths(grid) == 3

    def test_03(self):
        grid = [
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["O", "O", "O"],
        ]
        assert count_paths(grid) == 1

    def test_04(self):
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "X", "O", "O", "O"],
            ["X", "O", "X", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
        ]
        assert count_paths(grid) == 0

    def test_05(self):
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
            ["X", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
        ]
        assert count_paths(grid) == 42

    def test_06(self):
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
            ["X", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
        ]
        assert count_paths(grid) == 0

    def test_07(self):
        grid = [
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        assert count_paths(grid) == 40116600

    def test_08(self):
        grid = [
            ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
        ]
        assert count_paths(grid) == 3190434


if __name__ == "__main__":
    unittest.main()
