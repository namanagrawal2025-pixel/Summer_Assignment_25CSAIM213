def find_missing_number(arr, n):
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

def main():
    numbers = [1, 2, 4, 5, 6]
    total_elements = 6
    result = find_missing_number(numbers, total_elements)
    print(result)

main()
