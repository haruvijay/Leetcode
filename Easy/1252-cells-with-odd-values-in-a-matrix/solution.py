class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
            
        odd_rows = sum(1 for x in rows if x % 2 == 1)
        odd_cols = sum(1 for y in cols if y % 2 == 1)
        
        even_rows = m - odd_rows
        even_cols = n - odd_cols
        
        return odd_rows * even_cols + even_rows * odd_cols
