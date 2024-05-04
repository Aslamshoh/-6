#30.	Формируется матрица F следующим образом: если в В количество простых чисел в 	Формируется матрица F следующим образом: если в В количество простых чисел в 
3, то поменять в В симметрично области 1 и 3 местами, иначе С и В поменять местами 
несимметрично. При этом матрица А не меняется. После чего вычисляется выражение
((К*A T)*(F+А)-K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно
import numpy as np


# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Функция для формирования матрицы F
def form_matrix_F(matrix_B, matrix_C):
    num_primes_in_B = np.sum([is_prime(x) for x in matrix_B.flatten()])

    if num_primes_in_B == 3:
        matrix_B_symmetric = np.flip(matrix_B, axis=1)
        matrix_B[:, 0], matrix_B[:, 2] = matrix_B_symmetric[:, 2], matrix_B_symmetric[:, 0]
    else:
        matrix_B, matrix_C = matrix_C.copy(), matrix_B.copy()

    return matrix_B, matrix_C


# Функция для вычисления выражения ((К*A.T)*(F+A)-K*F.T)
def compute_expression(K, matrix_A, matrix_F):
    result = np.dot(K * matrix_A.T, matrix_F + matrix_A) - K * matrix_F.T
    return result


# Генерация матрицы А
def generate_matrix_A(N):
    return np.random.randint(-10, 11, (N, N))


# Основная функция
def main():
    K = float(input("Введите значение K: "))
    N = int(input("Введите размерность матрицы А (N): "))

    matrix_A = generate_matrix_A(N)
    matrix_B = generate_matrix_A(N)
    matrix_C = generate_matrix_A(N)

    print("Матрица A:")
    print(matrix_A)
    print("\nМатрица B:")
    print(matrix_B)
    print("\nМатрица C:")
    print(matrix_C)

    matrix_F_B, matrix_F_C = form_matrix_F(matrix_B, matrix_C)

    print("\nМатрица F, сформированная на основе матрицы B:")
    print(matrix_F_B)
    print("\nМатрица F, сформированная на основе матрицы C:")
    print(matrix_F_C)

    expression_result = compute_expression(K, matrix_A, matrix_F_B)
    print("\nРезультат вычисления выражения ((К*A.T)*(F+A)-K*F.T):")
    print(expression_result)


if __name__ == "__main__":
    main()

