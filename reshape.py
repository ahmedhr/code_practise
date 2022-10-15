# Reshape without intermediate single dimension array
from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m = len(mat)
    n = len(mat[0])
    res = list()
    if m * n != r * c:
        return mat
    p = q = 0
    for i in range(r):
        for j in range(c):
            if p < m:
                if q < len(mat[p]):
                    if i > len(res) - 1:
                        res.append([mat[p][q]])
                    else:
                        res[i].append(mat[p][q])
                    q += 1
                else:
                    p += 1
                    q = 0
                    if i > len(res) - 1:
                        res.append([mat[p][q]])
                    else:
                        res[i].append(mat[p][q])
                    q += 1
    return res


mat = [[1, 2, 4], [3, 4, 5]]
r = 3
c = 2

print(matrixReshape(mat, r, c))
