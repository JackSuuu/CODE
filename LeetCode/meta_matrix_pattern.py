"""
This is a meta software engineer coding assessment question

Given a matrix of integers, with each element containing either 0, 1, or 2, y
our task is to find the longest diagonal segment 
which matches the following pattern: 
1, 2, 0, 2, 0, 2, 0, ... 
(where the first element is 1, and then 2 and 0 are repeating infinitely), 
and finishes at a matrix border. Return the length of this diagonal segment.

The diagonal segment:

- May start at any matrix element
- May go toward any possible diagonal direction
- Must end at an element in the first or last row or column
"""

def solution(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    max_len = [0]  # Use list to modify in recursive calls
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def explore(i, j, length, di, dj):
        # Check if current position is on border
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            max_len[0] = max(max_len[0], length)
        
        # Calculate next position
        next_i = i + di
        next_j = j + dj
        
        # Check if next position is valid
        if not (0 <= next_i < n and 0 <= next_j < m):
            return
        
        # Expected value: 2 if length+1 is even, 0 if odd (since length=1 is 1)
        expected = 2 if (length + 1) % 2 == 0 else 0
        if matrix[next_i][next_j] != expected:
            return
        
        # Recurse with incremented length
        explore(next_i, next_j, length + 1, di, dj)
    
    # Iterate over all cells
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 1:
                continue
            # Try all four diagonal directions
            for di, dj in directions:
                explore(i, j, 1, di, dj)
    
    return max_len[0]