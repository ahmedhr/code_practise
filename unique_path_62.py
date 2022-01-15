
#https://leetcode.com/problems/unique-paths/

# Recusrsion

from collections import defaultdict


a = 3
b = 7

def uniquePaths(m: int, n: int, i=0, j=0) -> int:
    if i+1 == m and j+1 == n:
        return 1
    elif i < m and j < n:
        return uniquePaths(m, n, i+1, j) + uniquePaths(m, n, i, j+1)
    elif i == m or j == n:
        return 0

print(uniquePaths(a, b))



# Momoization + DP ~ Top-Bottom approach

def uniquePaths(m: int, n: int) -> int:
    memo = defaultdict(dict)
    return rec_uniquePaths(m, n, i=0, j=0, memo=memo)


def rec_uniquePaths(m: int, n: int, i=0, j=0, memo=None) -> int:
    if memo.get(i, {}).get(j):
        return memo[i][j]
    if i+1 == m and j+1 == n:
        return 1
    elif i < m and j < n:
        r = rec_uniquePaths(m, n, i+1, j,memo)
        c = rec_uniquePaths(m, n, i, j+1,memo)
        memo[i][j] =  r + c
        return memo[i][j]
    elif i == m or j == n:
        return 0

print(uniquePaths(a, b))



# Bottom-Top approach

def uniquePaths(m: int, n: int) -> int:
    memo = defaultdict(dict)
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                memo[i][j] = 1
                continue
            memo[i][j] = memo[i][j -1] + memo[i-1][j]
    return memo[m-1][n-1]

print(uniquePaths(a, b))