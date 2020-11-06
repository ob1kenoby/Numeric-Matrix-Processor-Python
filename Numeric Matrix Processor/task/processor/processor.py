def create_row_from_input(text=''):
    return [int(x) if x.find('.') < 0 else float(x) for x in input(text).split(" ")]


def create_matrix_from_input(order=""):
    size = create_row_from_input(f"Enter the size of {order}matrix: ")
    matrix = []
    print(f"Enter {order}matrix:")
    for i in range((size[0])):
        matrix.append(create_row_from_input())
    return matrix


def addition():
    a = create_matrix_from_input("first ")
    b = create_matrix_from_input("second ")
    error = False
    sum_ = []
    if len(a) == len(b):
        for i in range(len(a)):
            if len(a[i]) == len(b[i]):
                sum_.append([(a[i][j] + b[i][j]) for j in range(len(a[i]))])
            else:
                error = True
                break
    else:
        error = True
    if error:
        print("The operation cannot be performed, because the matrices are of different size.")
    else:
        output_result(sum_)


def multiplication_by_constant(matrix, c):
    if type(c) is str:
        if c.find('.') < 0:
            c = int(c)
        else:
            c = float(c)
    for i in range(len(matrix)):
        matrix[i] = [matrix[i][j] * c for j in range(len(matrix[i]))]
    return matrix


def multiplication_of_matrices():
    a = create_matrix_from_input("first ")
    b = create_matrix_from_input("second ")
    error = False
    result = []
    for row in a:
        intermediary = []
        if len(row) == len(b):
            for i in range(len(b[0])):
                x = 0
                for j in range(len(b)):
                    x += row[j] * b[j][i]
                intermediary.append(x)
        else:
            error = True
            break
        result.append(intermediary)
    if error:
        print("The operation cannot be performed")
    else:
        output_result(result)


def transpose_by_main(matrix):
    result = [[0 for _y in matrix] for _x in matrix[0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j][i] = matrix[i][j]
    return result


def transpose_by_side(matrix):
    result = [[0 for _y in matrix] for _x in matrix[0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[j][i] = matrix[len(matrix[i]) - 1 - i][len(matrix) - 1 - j]
    output_result(result)


def transpose_by_vertical(matrix):
    result = [[0 for _x in matrix[0]] for _y in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][len(matrix[i]) - 1 - j]
    output_result(result)


def transpose_by_horizontal(matrix):
    result = []
    while len(matrix) > 0:
        result.append(matrix.pop())
    output_result(result)


def output_result(matrix):
    print("The result is: ")
    for row in matrix:
        print(*row)


def transpose():
    print()
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = int(input("Your choice: "))
    matrix = create_matrix_from_input()
    if choice == 1:
        output_result(transpose_by_main(matrix))
    elif choice == 2:
        transpose_by_side(matrix)
    elif choice == 3:
        transpose_by_vertical(matrix)
    elif choice == 4:
        transpose_by_horizontal(matrix)


def create_minor_matrix(matrix, x, y=0):
    minor = [[0 for _x in range(len(matrix) - 1)] for _y in range(len(matrix) - 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i < y and j < x:
                minor[i][j] = matrix[i][j]
            elif i < y and j > x:
                minor[i][j - 1] = matrix[i][j]
            elif i > y and j < x:
                minor[i - 1][j] = matrix[i][j]
            elif i > y and j > x:
                minor[i - 1][j - 1] = matrix[i][j]
    return minor


def determinant(matrix):
    if len(matrix[0]) != len(matrix):
        print("The operation cannot be performed")
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            j = 1 if i % 2 == 0 else -1
            det += j * matrix[0][i] * determinant(create_minor_matrix(matrix, i))
        return det


def create_addition_matrix(matrix):
    a_addition = [[0 for _x in range(len(matrix))] for _y in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i + j) % 2 == 1:
                a_addition[i][j] = -matrix[i][j]
            else:
                a_addition[i][j] = matrix[i][j]
    return a_addition


def cofactor_matrix(matrix):
    cofactor = [[0 for _x in range(len(matrix))] for _y in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            cofactor[i][j] = determinant(create_minor_matrix(matrix, j, i))
    algebraic_addition = create_addition_matrix(cofactor)
    return transpose_by_main(algebraic_addition)


def inversion():
    matrix = create_matrix_from_input()
    output_result(multiplication_by_constant(cofactor_matrix(matrix), 1 / determinant(matrix)))


def main():
    choice = 10
    while choice:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = int(input("Your choice: "))
        if choice == 1:
            addition()
        elif choice == 2:
            matrix = create_matrix_from_input()
            c = input("Enter constant: ")
            output_result(multiplication_by_constant(matrix, c))
        elif choice == 3:
            multiplication_of_matrices()
        elif choice == 4:
            transpose()
        elif choice == 5:
            matrix = create_matrix_from_input()
            print(determinant(matrix))
        elif choice == 6:
            inversion()
        print()


if __name__ == "__main__":
    main()
