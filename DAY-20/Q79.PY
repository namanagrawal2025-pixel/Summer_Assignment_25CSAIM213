def find_row_sum(mat):
    row_sums = []
    for row in mat:
        total = sum(row)
        row_sums.append(total)
    return row_sums

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = find_row_sum(matrix)
    print(result)

main()
