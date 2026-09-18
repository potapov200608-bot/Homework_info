import numpy as np

def kramer(matrix_ext: np.array, N: int, M: int) -> list:

    matrix0 = matrix_ext.copy()
    matrix1 = np.delete(matrix_ext, M - 1, axis = 1)
    det1 = np.linalg.det(matrix1)

    if abs(np.linalg.det(matrix1)) < 1e-6:
        print("Система несовместна")
        return []
    ANS = []
    for i in range(M - 1):
        matrix = matrix0.copy()
        matrix[:, i] = matrix[:, M - 1]
        matrix = np.delete(matrix, M - 1, axis = 1)

        x = np.linalg.det(matrix)/det1
        ANS.append(float(x))
    return ANS


N, M = map(int, input().split())
matrix_ext = np.array([list(map(int, input().split())) for j in range(N)])

print(f"Решение: {kramer(matrix_ext, N, M)}")