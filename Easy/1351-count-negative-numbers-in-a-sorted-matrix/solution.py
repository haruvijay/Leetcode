class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = 0, n - 1
        neg_count = 0

        while row < m and col >= 0:
            if grid[row][col] < 0:
                neg_count += m - row
                col -= 1
            else:
                row += 1

        return neg_count
