def find_diagonal_sum(mat):
    n = len(mat)
    total_sum = 0
    for i in range(n):
        total_sum += mat[i][i]
    return total_sum

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = find_diagonal_sum(matrix)
    print(result)

main()
