def is_symmetric(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

def main():
    matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    result = is_symmetric(matrix)
    print(result)

main()
