import sys

def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices
    m = [[0] * (n+1) for _ in range(n+1)]

    # l = chain length
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[1][n]

# Example
p = [10, 30, 5, 60]  # Dimensions: A1(10x30), A2(30x5), A3(5x60)
print("Minimum multiplications:", matrix_chain_order(p))
