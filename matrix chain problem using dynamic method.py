def matrix_chain(p, n):
    m = [[0 for x in range(n)] for x in range(n)]

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (m[i][k] + m[k+1][j]
                        + p[i-1] * p[k] * p[j])

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n-1]


p = [10, 20, 30, 40, 30]

n = len(p)

print("Minimum number of multiplications:",
      matrix_chain(p, n))
