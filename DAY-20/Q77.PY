def multiply_matrices(mat1, mat2):
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    cols_mat2 = len(mat2[0])
    result = [[0] * cols_mat2 for _ in range(rows_mat1)]
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def main():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    result = multiply_matrices(m1, m2)
    print(result)

main()
