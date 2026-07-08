def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
    target_value = 25
    result = binary_search(sorted_numbers, target_value)
    print(result)

main()
