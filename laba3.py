#30.	Формируется матрица F следующим образом: если в В количество простых чисел в 	Формируется матрица F следующим образом: если в В количество простых чисел в 
3, то поменять в В симметрично области 1 и 3 местами, иначе С и В поменять местами 
несимметрично. При этом матрица А не меняется. После чего вычисляется выражение
((К*A T)*(F+А)-K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно
import numpy as np
import zlib

# Функция для поиска числителей в матрице
def find_divisible_numbers(matrix, divisor):
    divisible_numbers = []
    for number in matrix.flatten():
        if number % divisor == 0:
            divisible_numbers.append(number)
    return divisible_numbers
def main():
    K = float(input("Введите значение K: "))
    N = int(input("Введите размерность матрицы А (N): "))
    divisor = int(input("Введите число, на которое будем проверять деление: "))

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

    divisible_numbers_A = find_divisible_numbers(matrix_A, divisor)
    print(f"\nЧислители в матрице A, делящиеся на {divisor} без остатка:")
    print(divisible_numbers_A)

    divisible_numbers_B = find_divisible_numbers(matrix_B, divisor)
    print(f"\nЧислители в матрице B, делящиеся на {divisor} без остатка:")
    print(divisible_numbers_B)

    divisible_numbers_C = find_divisible_numbers(matrix_C, divisor)
    print(f"\nЧислители в матрице C, делящиеся на {divisor} без остатка:")
    print(divisible_numbers_C)


if __name__ == "__main__":
    main()
