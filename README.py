import numpy as np
from sympy import primerange


def generate_random_matrix(N):
    return np.random.randint(-10, 11, size=(N, N))


def count_primes_in_odd_columns(matrix):
    count = 0
    for j in range(1, matrix.shape[1], 2):  # Нечетные столбцы
        for i in range(matrix.shape[0]):
            if is_prime(matrix[i, j]):
                count += 1
    return count


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def swap_areas(matrix, area1, area3):
    temp = matrix[area1]
    matrix[area1] = matrix[area3]
    matrix[area3] = temp


def create_F(matrix_B, matrix_C):
    count_primes = count_primes_in_odd_columns(matrix_B)
    perimeter_product = np.prod([matrix_B[0, 0], matrix_B[0, -1], matrix_B[-1, -1], matrix_B[-1, 0]])
    if count_primes > perimeter_product:
        swap_areas(matrix_B, (0, 0), (-1, -1))
    else:
        matrix_B, matrix_C = matrix_C, matrix_B
    return matrix_B + matrix_C


def main(K, N):
    matrix_A = generate_random_matrix(N)
    matrix_B = generate_random_matrix(N // 2)
    matrix_C = generate_random_matrix(N // 2)
    matrix_F = create_F(matrix_B, matrix_C)

    result = (K * np.transpose(matrix_A) @ (matrix_F + matrix_A) - K * np.transpose(matrix_F))

    print("Matrix A:")
    print(matrix_A)
    print("\nMatrix F:")
    print(matrix_F)
    print("\nResult:")
    print(result)


# Пример использования
K = 2
N = 4
main(K, N)
