def findDiagonalOrder(mat):
    if not mat or not mat[0]:
        return []
    m, n = len(mat), len(mat[0])
    result = []
    for d in range(m + n - 1):  # Total diagonals
        if d % 2 == 0:  # Up-right direction
            i = min(d, m-1)
            j = d - i
            while i >= 0 and j < n:
                result.append(mat[i][j])
                i -= 1
                j += 1
        else:  # Down-left
            j = min(d, n-1)
            i = d - j
            while j >= 0 and i < m:
                result.append(mat[i][j])
                i += 1
                j -= 1
    return result

# Test: [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,4,7,5,3,6,8,9]
print(findDiagonalOrder(mat=[[1,2,3],[4,5,6],[7,8,9]]))