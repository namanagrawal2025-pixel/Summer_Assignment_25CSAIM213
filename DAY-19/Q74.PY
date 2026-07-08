def subtract_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] - mat2[i][j]
    return result

def main():
    m1 = [[5, 6], [7, 8]]
    m2 = [[1, 2], [3, 4]]
    result = subtract_matrices(m1, m2)
    print(result)

main()
