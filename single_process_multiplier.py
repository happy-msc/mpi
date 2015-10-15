from random import randint

X = []
Y = []
Z = []

N = 500


def init_matrix():
    """
    Initialize matrxi from here, we do initialize three matrx from here
        1. mtrx1 - input matrix
        2. mtrx2 - input matrix
        3. mtrx3 - output matrix
    """
    global X
    X = [[randint(0, 9) for i in range(N)] for j in range(N)]

    global Y
    Y = [[randint(0, 9) for i in range(N)] for j in range(N)]


def multiply_matrix(X, Y):
    """
    Generate new matrix by multiplying incoming matrix data. Following is the
    algorithm for matrix multiplication

    X = [
            [1, 2, 3, 4],
            [3, 2, 3, 7],
        ]

    Y = [
            [1, 2, 3],
            [5, 6, 7],
            [2, 2, 7],
            [5, 6, 9],
        ]

    Z = [
            [(1*1 + 2*5 + 3*2 + 4*5), (1*2 + 2*6 + 3*2 + 4*6), --, --],
            [(3*1 + 2*5 + 3*2 + 7*5), (3*2 + 2*6 + 3*2 + 7*6), --, --]
        ]

    Args:
        X: rows of mtrx1
        Y: whole mtrx2

    Returns:
        Z: calculated matrix part
    """
    Z = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)]
            for X_row in X]

    print Z


if __name__ == '__main__':
    """
    Main method here, we have to do
        1. initilize matrxies
        2. Multiply matrix
    """
    init_matrix()
    multiply_matrix(X, Y)


'''
#Z = [[0] * N for i in range(N)]
Z = [[0] * len(mtrx2[0]) for i in range(len(mtrx1))]

i = 0
for a in mtrx1:
    j = 0
    for b in a:
        k = 0
        for c in mtrx2[j]:
            Z[i][k] = Z[i][k] + (b * c)
            k = k + 1
        j = j + 1
    i = i + 1
'''
