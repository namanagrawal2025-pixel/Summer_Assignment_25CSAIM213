def transpose_matrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = mat[i][j]
    return result

def main():
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = transpose_matrix(matrix)
    print(result)

main()
