def find_column_sum(mat):
    rows = len(mat)
    cols = len(mat[0])
    col_sums = []
    for j in range(cols):
        total = 0
        for i in range(rows):
            total += mat[i][j]
        col_sums.append(total)
    return col_sums

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = find_column_sum(matrix)
    print(result)

main()
